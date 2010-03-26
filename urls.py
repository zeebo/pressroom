from django.conf.urls.defaults import *
from pressroom.settings import MEDIA_ROOT
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
#  (r'^register/', include(reg_patterns)),
#  (r'^accounts/', include(auth_patterns)),
#  (r'^companies/', include(company_patterns)),
#  (r'^releases/', include(post_patterns)),
  (r'^admin/', include(admin.site.urls)),
  (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
  (r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'base.html'}),
)
