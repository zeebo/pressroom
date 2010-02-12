from django.conf.urls.defaults import *
from pressroom.post.models import Post
from django.contrib.auth.models import Group
from django.core.urlresolvers import reverse

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  (r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'base.html'}, 'root'),
)

post_info = {
  'queryset': Post.objects.all(),
}
group_info = {
  'queryset': Group.objects.all(),
}

reg_patterns = patterns('pressroom.register.views',
  (r'^$', 'register'),
  (r'^(?P<token>[0-9a-f]+)/$', 'activate'),
)

auth_patterns = patterns('django.contrib.auth.views',
  (r'^login/$', 'login', {'template_name': 'register/login.html'}),
  (r'^logout/$', 'logout', {'template_name': 'register/logout.html', 'next_page' : '/'})
)

group_patterns = patterns('',
  (r'^$', 'django.views.generic.list_detail.object_list', group_info, 'list_groups'),
  (r'^(?P<group_name>\w+)/$', 'pressroom.groups.views.group_detail'),
  (r'^(?P<group_name>\w+)/join/$', 'pressroom.groups.views.add_group'),
  (r'^(?P<group_name>\w+)/part/$', 'pressroom.groups.views.del_group'),
)

post_patterns = patterns('',
  (r'^$', 'django.views.generic.list_detail.object_list', post_info, 'list_posts'),
  (r'^(?P<group_name>\w+)/$', 'pressroom.post.views.post_list_for'),
  (r'^(?P<group_name>\w+)/(?P<slug>[\w-]+)/$', 'pressroom.post.views.post_detail'),
)

urlpatterns += patterns('',
  (r'^register/', include(reg_patterns)),
  (r'^accounts/', include(auth_patterns)),
  (r'^companies/', include(group_patterns)),
  (r'^releases/', include(post_patterns)),
  (r'^admin/', include(admin.site.urls)),
)
