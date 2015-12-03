from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from survey.models import autum
import re
# Create your views here.
def index(request):
    context={}
    branchinfo = {
        '0071':'pdjs',
        '0169':'pdyyl',
        '0332':'pdcy',
        '0333':'pdyyzx',
        '0335':'pddd',
    }
    js=len(autum.objects.filter(branch='0071',hly=True))+len(autum.objects.filter(branch='0071',skb=True))+len(autum.objects.filter(branch='0071',sxt=True))+len(autum.objects.filter(branch='0071',kkt=True))+len(autum.objects.filter(branch='0071',tlkh=True))
    yyl=len(autum.objects.filter(branch='0169',hly=True))+len(autum.objects.filter(branch='0169',skb=True))+len(autum.objects.filter(branch='0169',sxt=True))+len(autum.objects.filter(branch='0169',kkt=True))+len(autum.objects.filter(branch='0169',tlkh=True))
    cy=len(autum.objects.filter(branch='0332',hly=True))+len(autum.objects.filter(branch='0332',skb=True))+len(autum.objects.filter(branch='0332',sxt=True))+len(autum.objects.filter(branch='0332',kkt=True))+len(autum.objects.filter(branch='0332',tlkh=True))
    yyzx=len(autum.objects.filter(branch='0333',hly=True))+len(autum.objects.filter(branch='0333',skb=True))+len(autum.objects.filter(branch='0333',sxt=True))+len(autum.objects.filter(branch='0333',kkt=True))+len(autum.objects.filter(branch='0333',tlkh=True))
    dd=len(autum.objects.filter(branch='0335',hly=True))+len(autum.objects.filter(branch='0335',skb=True))+len(autum.objects.filter(branch='0335',sxt=True))+len(autum.objects.filter(branch='0335',kkt=True))+len(autum.objects.filter(branch='0335',tlkh=True))
    hj=js+yyl+cy+yyzx+dd
    context={
        'js': js,
        'yyl': yyl,
        'cy': cy,
        'yyzx':yyzx,
        'dd': dd,
        'sum': hj
    }
    for branch in branchinfo.keys():
        hly=skb=sxt=kkt=tlkh=0
        for temp in autum.objects.filter(branch=branch).values():
            if temp['hly']==True:
                hly+=1
            if temp['skb']==True:
                skb+=1
            if temp['sxt']==True:
                sxt+=1
            if temp['kkt']==True:
                kkt+=1
            if temp['tlkh']==True:
                tlkh+=1
        context['%s'%branchinfo[branch]]='%s,%s,%s,%s,%s' %(hly,skb,sxt,kkt,tlkh)

    return render(request,'survey/index.html',context)
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
        if len(request.GET['ID'])==15 or len(request.GET['ID'])==18:
            record.ID_card=request.GET['ID']
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
        else:
            context['result']='身份证号输入有误'

    return render(request,'survey/done.html',context)
def error(request):
    return render(request,'survey/error.html')
def dtails(request):
    context={}
    context['branch']=request.GET['branch']
    branchinfo = {
        '0071':'九沙支行',
        '0169':'月雅路支行',
        '0332':'朝阳支行',
        '0333':'营业中心',
        '0335':'德胜东路支行',
    }
    context['branch_name']=branchinfo[request.GET['branch']]
    names=[]
    temps=autum.objects.filter(branch=request.GET['branch']).values('worker')
    for temp in temps:
        names.append(temp['worker'])
    name={}
    for i in names:
        if names.count(i)>=1:
            name[i]=names.count(i)
    sum=0
    for i in name.values():
        sum+=i
    chart_name=[]
    chart_y=[]
    for key in name.keys():
        name[key]=name[key]/sum
        chart_name=key
    context['chart_name']=chart_name
    context['name']=name
    records=autum.objects.filter(branch=request.GET['branch']).values().order_by('time')
    ls_all=[]
    for record in records:
        ls=[]
        for vb in record.keys():
            if record[vb]==False:
                record[vb]='否'
            if record[vb]==True:
                record[vb]='是'
        ls.append(record['name'])
        ls.append(record['market'])
        ls.append(record['hly'])
        ls.append(record['skb'])
        ls.append(record['sxt'])
        ls.append(record['kkt'])
        ls.append(record['tlkh'])
        ls.append(record['worker'])
        ls.append(record['note'])
        ls_all.append(ls)
    context['ls_all']=ls_all

    return render(request,'survey/details.html',context)