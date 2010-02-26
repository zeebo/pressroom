from django.conf.urls.defaults import *
from pressroom.posts.models import Post
from pressroom.posts.views import CompanyRSSFeed, PostRSSFeed
from pressroom.companies.models import Company
from pressroom.settings import MEDIA_ROOT

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

company_info = {
  'queryset': Company.objects.all(),
}

reg_patterns = patterns('pressroom.register.views',
  (r'^$', 'register'),
  (r'^(?P<token>[0-9a-f]+)/$', 'activate'),
)

auth_patterns = patterns('django.contrib.auth.views',
  (r'^login/$', 'login', {'template_name': 'register/login.html'}),
  (r'^logout/$', 'logout', {'template_name': 'register/logout.html', 'next_page' : '/'})
)

company_patterns = patterns('',
  (r'^$', 'django.views.generic.list_detail.object_list', company_info, 'list_companiess'),
  (r'^(?P<company_name>\w+)/$', 'pressroom.companies.views.company_detail'),
  (r'^(?P<company_name>\w+)/join/$', 'pressroom.companies.views.join_company_list'),
  (r'^(?P<company_name>\w+)/part/$', 'pressroom.companies.views.part_company_list'),
)

post_patterns = patterns('pressroom.posts.views',
  (r'^$', 'post_list'),
  (r'^rss\.xml$', PostRSSFeed()),
  (r'^(?P<group_name>\w+)/$', 'post_list_for'),
  (r'^(?P<group_name>\w+)/(?P<slug>[\w-]+)/$', 'post_detail'),
  (r'^(?P<group_name>\w+)/rss\.xml$', CompanyRSSFeed()),
)

urlpatterns = patterns('',
  (r'^register/', include(reg_patterns)),
  (r'^accounts/', include(auth_patterns)),
  (r'^companies/', include(company_patterns)),
  (r'^releases/', include(post_patterns)),
  (r'^admin/', include(admin.site.urls)),
  (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
  (r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'base.html'}),
)
