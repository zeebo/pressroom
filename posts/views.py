from django.views.generic.list_detail import object_list, object_detail
from pressroom.posts.models import Post

def post_list_for(request, group_name):
  post_set = Post.objects.filter(company__name__exact=group_name)
  return object_list(request, queryset=post_set)
  

def post_detail(request, group_name, slug):
  post_set = Post.objects.filter(company__name__exact=group_name)
  return object_detail(request, queryset=post_set, slug=slug)