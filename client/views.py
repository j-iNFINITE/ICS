from login.form import UserForm, UserProfileForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from client.models import client_info
# Create your views here.
@login_required
def index(request):
    context_dict={}
    context=[]
    clients = client_info.objects.all()
    for client in clients:
        if client.client_MANAGER.username==request.user.username:
            context.append(client.client_NAME)
    context_dict['clients'] = context
    return render(request,'client-index.html',context_dict)

@login_required
def client(request):
    context={}
    context['client']=request.GET['client']
    info=client_info.objects.get(client_NAME=request.GET['client'])
    if info.client_GENDER=='M':
        context['gender']='男'
    else:
        context['gender']='女'
    context['phone']=info.client_PHONE
    context['market']=info.client_MARKET
    context['address']=info.client_ADDRESS

    return render(request, 'client-info.html',context)
@login_required
def pd(request):
    client=request.GET['client']
    return render(request, 'client-pd.html',{'client':client})
@login_required
def need(request):
    client=request.GET['client']
    return render(request, 'client-need.html',{'client':client})