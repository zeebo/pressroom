from django.db import models
from django.contrib.auth.models import Group
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.template.defaultfilters import slugify
import datetime

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=100)
  body = models.TextField()
  slug = models.SlugField(max_length=50, editable=False)
  company = models.ForeignKey(Group)
  time_released = models.DateTimeField()
  
  def was_published_today(self):
    return self.time_released.date() == datetime.date.today()
    
  def display_body(self):
    return mark_safe(self.body)
    
  def save(self):
    if not self.id:
      self.slug = slugify(self.title)
    super(self.__class__, self).save()


class PostAdmin(admin.ModelAdmin):
  list_display = ('slug', 'company', 'time_released', 'was_published_today')