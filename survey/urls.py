from django.conf.urls import patterns,url
import survey.views
urlpatterns = [
    url(r'^$', survey.views.index, name='index'),

]
