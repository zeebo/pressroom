from django.views.generic.list_detail import object_list, object_detail
from django.contrib.syndication.views import Feed
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from pressroom.posts.models import Post
from datetime import datetime

def post_set():
  return Post.objects.filter(time_released__lte=datetime.now())

def post_list(request):
  return object_list(request, queryset=post_set())

def post_list_for(request, group_name):
  return object_list(request, queryset=post_set().filter(company__name__exact=group_name))
  
def post_detail(request, group_name, slug):
  return object_detail(request, queryset=post_set().filter(company__name__exact=group_name), slug=slug)
  

class CompanyRSSFeed(Feed):
  def title(self, obj):
    return "%s news feed" % obj.name
  
  def get_object(self, request, group_name):
    return get_object_or_404(Group, name=group_name)
    
  def link(self, obj):
    return reverse('pressroom.groups.views.group_detail', kwargs={'group_name':obj.name})
  
  def description(self, obj):
    return "News releases and important information for %s" % obj.name
  
  def items(self, obj):
    return post_set().filter(company__name=obj.name).order_by('-time_released')[:5]
    
  def item_title(self, item):
    return item.title
  
  def item_description(self, item):
    return item.description()

class PostRSSFeed(Feed):
  title = "Yes International Press Releases"
  description = "News releases and important information"
  
  def link(self):
    return reverse('pressroom.posts.views.post_list')
    
  def items(self):
    return post_set().order_by('-time_released')[:10]
    
  def item_title(self, item):
    return "%s: %s" % (item.company.name, item.title)
    
  def item_description(self, item):
    return item.description()