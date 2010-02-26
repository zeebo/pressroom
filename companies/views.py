# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.list_detail import object_detail
from django.contrib import messages
from pressroom.companies.models import Company

@login_required
def join_company_list(request, company_name):
  company = get_object_or_404(Company, group__name=company_name)
  request.user.groups.add(company.group)
  messages.success(request, "Added to %s email list." % company.full_name)
  return HttpResponseRedirect(reverse(company_detail, kwargs={'company_name':company.group.name}))

@login_required
def part_company_list(request, company_name):
  company = get_object_or_404(Company, group__name=company_name)
  request.user.groups.remove(company.group)
  messages.success(request, "Removed from %s email list." % company.full_name)
  return HttpResponseRedirect(reverse(company_detail, kwargs={'company_name':company.group.name}))

def company_detail(request, company_name):
  company_set = Company.objects.filter(group__name__exact=company_name)
  company = get_object_or_404(Company, group__name=company_name)
  return object_detail(request, queryset=company_set, object_id=company.pk)
  