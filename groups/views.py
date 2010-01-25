from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User, Group
from django.http import HttpResponse, HttpResponseRedirect

@login_required
def add_group(request, group_name):
  group = get_object_or_404(Group, name=group_name)
  request.user.groups.add(group)
  request.user.message_set.create(message="Added to %s email list." % group_name)
  return HttpResponseRedirect('/companies/%s/' % group_name) #Fix to be generic
  
@login_required
def del_group(request, group_name):
  group = get_object_or_404(Group, name=group_name)
  request.user.groups.remove(group)
  request.user.message_set.create(message="Removed from %s email list." % group_name)
  return HttpResponseRedirect('/companies/%s/' % group_name) #Fix to be generic


#Fix to get message set for the group
def view_group(request, group_name):
  group = get_object_or_404(Group, name=group_name)
  return HttpResponse("Will have list of releases!")

#Fix to be generic view
def list_groups(request):
  return HttpResponse("Will have a list of groups!")
