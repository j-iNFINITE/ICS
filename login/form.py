from django import forms
from django.contrib.auth.models import User
from login.models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(label= '密码',widget=forms.PasswordInput())
    username = forms.CharField(label='姓名')
    class Meta:
        model = User
        fields = ('username', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('branch','phone')
