from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group
from django import forms

class MyUserAdminForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ('email', 'password', 'groups', )

class MyUserAdmin(admin.ModelAdmin):
  list_filter = ('last_login', 'date_joined', )
  list_display = ('email', 'last_login', 'date_joined', )
  search_fields = ('email', )
  form = MyUserAdminForm

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, MyUserAdmin)