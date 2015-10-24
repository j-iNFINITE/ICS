from login.form import UserForm, UserProfileForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
    return render(request,'client-index.html')

@login_required
def client(request):
    client=request.GET['client']
    return render(request,'client-client.html',{'client':client})