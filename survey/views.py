from login.form import UserForm, UserProfileForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
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
def survey(request):
    context={}
    context['branch']=request.GET['branch']
    context['worker']=request.GET['worker']
    return render(request,'survey/survey.html',context)
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
        record.worker=context['worker']
        record.market=context['market']
        record.branch=branchinfo[context['branch']]
        record.save()
        context['result']='登记完成'

    return render(request,'survey/done.html',context)
