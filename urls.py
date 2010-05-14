from django.conf.urls.defaults import *
from pressroom.settings import MEDIA_ROOT
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  (r'^', include('companies.urls')),
  (r'^auth/login/$', 'django.contrib.auth.views.login'),
  (r'^auth/', include('register.urls')),
  (r'^admin/', include(admin.site.urls)),
  (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
  (r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'base.html'}),
)
