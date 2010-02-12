from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User, Group
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.list_detail import object_detail

@login_required
def add_group(request, group_name):
  group = get_object_or_404(Group, name=group_name)
  request.user.groups.add(group)
  request.user.message_set.create(message="Added to %s email list." % group_name)
  return HttpResponseRedirect(reverse(group_detail, kwargs={'group_name':group_name}))

@login_required
def del_group(request, group_name):
  group = get_object_or_404(Group, name=group_name)
  request.user.groups.remove(group)
  request.user.message_set.create(message="Removed from %s email list." % group_name)
  return HttpResponseRedirect(reverse(group_detail, kwargs={'group_name':group_name}))

def group_detail(request, group_name):
  group_set = Group.objects.filter(name__exact=group_name)
  group = get_object_or_404(Group, name=group_name)
  return object_detail(request, queryset=group_set, object_id=group.pk)
  