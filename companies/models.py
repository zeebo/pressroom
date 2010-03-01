from django.db import models
from django.contrib.auth.models import Group
from django.contrib import admin
from django import forms


# Create your models here.
class Company(models.Model):
  group = models.OneToOneField(Group, primary_key=True)
  full_name = models.CharField(max_length=100)
  stock_ticker = models.CharField(max_length=10)
  blurb = models.TextField()
  website = models.URLField()
  active = models.BooleanField(default=True)
  
  class Meta:
    verbose_name_plural = 'Companies'
  
  #Dont allow the model to be deleted.
  #Use the inactive field instead.
  def delete(self, *args, **kwargs):
    self.active = False
    self.save()
    

class CompanyAdminForm(forms.ModelForm):
  class Meta:
    model = Company
    fields = ('full_name', 'short_name', 'stock_ticker', 'website', 'blurb')
  
  #Add a field to abstract the group model from user interaction
  short_name = forms.CharField(max_length=100, required=True)
  
  def __init__(self, *args, **kwargs):
    #Populate the short_name field if in edit mode (instance is defined)
    if 'instance' in kwargs:
      self.declared_fields['short_name'].initial = kwargs['instance'].group.name
      
    forms.ModelForm.__init__(self, *args, **kwargs)
  
  def clean_short_name(self):
    
    #Check to see if the group is defined on the instance
    #If so we are in edit mode
    instance_group = None
    try:
      instance_group = self.instance.group
    except Group.DoesNotExist:
      pass
    
    #If we're in edit mode, dont allow short_name to be changed
    if 'short_name' in self.changed_data and instance_group:
      raise forms.ValidationError('Can\'t change the short name for a company')
    else:
      self.group, created = Group.objects.get_or_create(name=self.cleaned_data['short_name'])
    
class CompanyAdmin(admin.ModelAdmin):
  list_display = ('full_name', 'group', 'active')
  form = CompanyAdminForm
  
  actions = ('make_inactive', 'make_active', )
  
  def make_inactive(self, request, queryset):
    queryset.update(active=False)
  make_inactive.short_description = "Mark selected companies as inactive"
  
  def make_active(self, request, queryset):
    queryset.update(active=True)
  make_active.short_description = "Mark selected companies as active"
  
  #Remove delete from the list of actions to force active/inactive.
  def get_actions(self, request):
    actions = super(CompanyAdmin, self).get_actions(request)
    del actions['delete_selected']
    return actions