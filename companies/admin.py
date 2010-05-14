from models import Company, Post
from django.contrib.auth.models import User, Group
from django.contrib import admin
from django import forms

class PostAdmin(admin.ModelAdmin):
  list_display = ('slug', 'company', 'time_released', 'was_published_today')

class CompanyAdmin(admin.ModelAdmin):
  list_display = ('full_name', 'number_of_users')

class MyUserAdminForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ('email', 'password', )

class MyUserAdmin(admin.ModelAdmin):
  list_filter = ('last_login', 'date_joined', )
  list_display = ('email', 'last_login', 'date_joined', )
  search_fields = ('email', )
  form = MyUserAdminForm

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, MyUserAdmin)

admin.site.register(Post, PostAdmin)
admin.site.register(Company, CompanyAdmin)