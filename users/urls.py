from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'login/', 'users.views.user_login'),
                       )
