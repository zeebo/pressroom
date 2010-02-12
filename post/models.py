from django.db import models
from django.contrib.auth.models import Group
from django.contrib import admin
from django.utils.safestring import mark_safe
import datetime

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=100)
  body = models.TextField()
  slug = models.SlugField(max_length=50)
  company = models.ForeignKey(Group)
  time_released = models.DateTimeField()
  
  def was_published_today(self):
    return self.time_released.date() == datetime.date.today()
    
  def display_body(self):
    return mark_safe(self.body)


class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title", )}
  list_display = ('slug', 'company', 'time_released', 'was_published_today')