from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils.safestring import mark_safe
import datetime

class Company(models.Model):
  full_name = models.CharField(max_length=100)
  stock_ticker = models.CharField(max_length=10, unique=True)
  blurb = models.TextField()
  website = models.URLField()
  users = models.ManyToManyField(User, related_name="companies", blank=True)
  
  @models.permalink
  def get_absolute_url(self):
    return ('companies.views.company_detail', (),  {'stock_ticker':self.stock_ticker})
  
  def __unicode__(self):
    return self.full_name
  
  def number_of_users(self):
    return self.users.count()
  
  class Meta:
    verbose_name_plural = 'Companies'

class Post(models.Model):
  title = models.CharField(max_length=100)
  body = models.TextField()
  slug = models.SlugField(max_length=50, editable=False)
  company = models.ForeignKey(Company, related_name="posts")
  time_released = models.DateTimeField()
  
  @models.permalink
  def get_absolute_url(self):
    return ('companies.views.post_detail', (), {'slug':self.slug, 'stock_ticker':self.company.stock_ticker})
  
  def __unicode__(self):
    return self.title
  
  def was_published_today(self):
    return self.time_released.date() == datetime.date.today()
    
  def display_body(self):
    return mark_safe(self.body)
    
  def save(self):
    if not self.id:
      self.slug = slugify(self.title)
    super(self.__class__, self).save()
  
  def description(self):
    return self.display_body()[:100]
