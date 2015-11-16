from django.conf.urls import patterns,url
import survey.views
urlpatterns = [
    url(r'^$', survey.views.index, name='index'),
    url(r'^test$', survey.views.test, name='test'),
    url(r'^survey$', survey.views.survey, name='survey'),
    url(r'^.*-done$', survey.views.done, name='done'),
    url(r'^login$', survey.views.login, name='login'),

]
