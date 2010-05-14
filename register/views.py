from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from forms import RegistrationForm
from models import RegistrationToken
import random
import hashlib

def sha(data=None, len=0):
  if data is None:
    data = random.random()
      
  digest = hashlib.sha1(str(data)).hexdigest()
  if len == 0:
    return digest
  return digest[:len]

def render_to(template):
  def decorator(function):
    def dec_func(request, *args, **kwargs):
      return render_to_response(template, function(request, *args, **kwargs), context_instance=RequestContext(request))
    return dec_func
  return decorator

@render_to('register/register.html')
def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      #Make a new (inactive) user, and mail out the registration token
      new_user = User(username=sha(form.cleaned_data['email'], 30), is_active=False, **form.cleaned_data)
      new_user.set_password(form.cleaned_data['password'])
      new_user.save()
      
      new_token = RegistrationToken(user=new_user, token=sha(len=10))
      new_token.save()
      
      #change to we mailed you, and click link plz
      return {'message':"Valid form! Your token is %s" % new_token.token}
  else:
    form = RegistrationForm()
  
  return {'form':form}

def activate(request, token):
  reg_token = get_object_or_404(RegistrationToken, token=token)
  reg_token.user.is_active = True
  reg_token.user.save()
  
  reg_token.delete()
  
  #change to message framework
  return HttpResponse("User activated.")
  