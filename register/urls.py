from django.conf.urls.defaults import *

urlpatterns = patterns('register.views',
  (r'^register/$', 'register'),
  (r'^activate/(?P<token>[0-9a-fA-F]*)/$', 'activate'),
)