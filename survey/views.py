from login.form import UserForm, UserProfileForm
from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from survey.models import autum
import re
# Create your views here.
def index(request):
    return render(request,'survey/index.html')
def test(request):
    context={}
    context['branch']=request.GET['branch']
    context['worker']=request.GET['worker']
    return render(request,'survey/test.html',context)
@login_required
def survey(request):
    context={}
    context['branch']=request.GET['branch']
    context['worker']=request.GET['worker']
    return render(request,'survey/survey.html',context)
def login(request):
    if request.method == 'POST':
        context={}
        context['branch']=request.POST['branch']
        context['name']=request.POST['name']
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('name')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                auth_login(request, user)
                return HttpResponseRedirect('/survey/survey?branch=%s&worker=%s' %(context['branch'],context['name']))
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("账户无效")
        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("账号有误，请退回重试")
    else:
        context={}
        context['branch']=request.GET['branch']
        context['worker']=request.GET['worker']
    return render(request,'survey/login.html',context)
@login_required
def done(request):
    context={}
    branchinfo={
        '九沙支行':'0071',
        '月雅路支行':'0169',
        '朝阳支行':'0332',
        '营业中心':'0333',
        '德胜东路支行':'0335'
    }
    string=request.path
    pattern = re.compile(r'/survey/(.*?)-(.*?)-')
    match = pattern.match(string)
    context['branch']=match.group(1)
    context['worker']=match.group(2)
    context['name']=request.GET['name']
    context['market']=request.GET['market']
    try:
        record=autum.objects.get(name=context['name'])
        context['result']='已有记录!'

    except autum.DoesNotExist:
        record = autum(name=context['name'])
        if 'hly' in request.GET.keys():
            record.hly=request.GET['hly']
        if 'skb' in request.GET.keys():
            record.skb=request.GET['skb']
        if 'kkt' in request.GET.keys():
            record.kkt=request.GET['kkt']
        if 'sxt' in request.GET.keys():
            record.sxt=request.GET['sxt']
        if 'tlkh' in request.GET.keys():
            record.tlkh=request.GET['tlkh']
        if 'note' in request.GET.keys():
            record.note=request.GET['note']
        record.worker=context['worker']
        record.market=context['market']
        record.branch=branchinfo[context['branch']]
        record.save()
        context['result']='登记完成'

    return render(request,'survey/done.html',context)
def error(request):
    return render(request,'survey/error.html')