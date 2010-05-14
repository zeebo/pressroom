from django.conf.urls.defaults import *

urlpatterns = patterns('companies.views',
  (r'^companies/$', 'company_list'),
  (r'^companies/(?P<stock_ticker>.*)/$', 'company_detail'),
  (r'^news/$', 'post_list'),
  (r'^news/(?P<stock_ticker>[^/]+)/$', 'post_list_for'),
  (r'^news/(?P<stock_ticker>[^/]+)/(?P<slug>.*)$', 'post_detail'),
)