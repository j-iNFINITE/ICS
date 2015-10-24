from django.conf.urls import patterns,url
from client import views
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'client-client$',views.client,name='client')
    )
