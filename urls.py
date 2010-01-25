from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

reg_patterns = patterns('pressroom.register.views',
  (r'^$', 'register'),
  (r'^(?P<token>[0-9a-f]+)/$', 'activate'),
)

auth_patterns = patterns('django.contrib.auth.views',
  (r'^login/$', 'login', {'template_name': 'register/login.html'}),
  (r'^logout/$', 'logout', {'template_name': 'register/logout.html', 'next_page' : '/'})
)

urlpatterns = patterns('',
  (r'^reg/', include(reg_patterns)),
  (r'^auth/', include(auth_patterns)),
  (r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'base.html'}),
  (r'^admin/', include(admin.site.urls)),
)
