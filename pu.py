import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ICS.settings')
import django
django.setup()
from login.form import UserForm, UserProfileForm
from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from survey.models import autum
import re
context={}
branchinfo = {
    '0071':'pdjs',
    '0169':'pdyyl',
    '0332':'pdcy',
    '0333':'pdyyzx',
    '0335':'pddd',
}
js=autum.objects.filter(branch='0071')
yyl=autum.objects.filter(branch='0169')
cy=autum.objects.filter(branch='0332')
yyzx=autum.objects.filter(branch='0333')
dd=autum.objects.filter(branch='0335')
hj=len(js)+len(yyl)+len(cy)+len(yyzx)+len(dd)
context={
    'js': len(js),
    'yyl': len(yyl),
    'cy': len(cy),
    'yyzx':len(yyzx),
    'dd': len(dd),
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
    context['%s'%branchinfo[branch]]=[hly,skb,sxt,kkt,tlkh]

print(context)