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
ls_all=[]

records=autum.objects.filter(branch='0071').values()
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

print(ls_all)