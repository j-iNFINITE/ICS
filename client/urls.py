from django.conf.urls import patterns,url
from client import views
urlpatterns = patterns('',
                        url(r'^$', views.index, name='index'),
                        url(r'client-client$',views.client,name='client'),
                        url(r'client-client-pd$',views.pd,name='pd'),
                       url(r'client-client-need$',views.need,name='need')

                       )
