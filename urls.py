from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

reg_patterns = patterns('pressroom.register.views',
    (r'^$', 'register'),
    (r'^(?P<token>[0-9a-f]+)/$', 'activate'),
)

urlpatterns = patterns('',
    (r'^reg/', include(reg_patterns)),
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'base.html'}),
    (r'^admin/', include(admin.site.urls)),
)
