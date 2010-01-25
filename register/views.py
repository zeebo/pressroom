# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from pressroom.register.forms import RegistrationForm
from pressroom.register.models import RegistrationToken
from pressroom.utils import sha
from django.contrib.auth.models import User
import hashlib, random

def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      #Make a new (inactive) user, and mail out the registration token
      new_user = User(username=sha(form.cleaned_data['email']), 30), is_active=False, **form.cleaned_data)
      new_user.set_password(form.cleaned_data['password'])
      new_user.save()
      
      new_token = RegistrationToken(user=new_user, token=sha(len=10))
      new_token.save()
      return HttpResponse("Valid form! Your token is %s" % new_token.token)
  else:
    form = RegistrationForm()
  
  return render_to_response('register/register.html', {'form':form})

def activate(request, token):
  reg_token = get_object_or_404(RegistrationToken, token=token)
  reg_token.user.is_active = True
  reg_token.user.save()
  
  reg_token.delete()
  
  return HttpResponse("User activated.")
  