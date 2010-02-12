from django.db import models
from django.contrib.auth.models import Group
from django.contrib import admin

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=100)
  body = models.TextField()
  slug = models.SlugField(max_length=50)
  company = models.ForeignKey(Group)
  time_released = models.DateTimeField()

class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title", )}