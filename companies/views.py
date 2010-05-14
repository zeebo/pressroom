from models import Company, Post
from django.views.generic.list_detail import object_list, object_detail

#Some generic views yeahhhhhh

def company_list(request):
  """
  List companies for people to look at. Possibly put companies you're part of at the top
  """
  return object_list(request, Company.objects.all())

def company_detail(request, stock_ticker):
  """
  Show the last few posts for the company
  """
  return object_detail(request, Company.objects.all(), slug=stock_ticker, slug_field='stock_ticker')

def post_list(request):
  """
  List of most recent news posts
  """
  return object_list(request, Post.objects.all())

def post_list_for(request, stock_ticker):
  """
  List of posts for a company
  """
  return object_list(request, Post.objects.filter(company__stock_ticker=stock_ticker))

def post_detail(request, stock_ticker, slug):
  """
  Detail on a post
  """
  return object_detail(request, Post.objects.filter(company__stock_ticker=stock_ticker), slug=slug)