from django.conf.urls import patterns,url
from client import views
urlpatterns = patterns('',
                        url(r'^$', views.index, name='index'),
                        url(r'client-info$',views.client,name='client'),
                        url(r'client-pd$',views.pd,name='pd'),
                       url(r'client-need$',views.need,name='need')

                       )
