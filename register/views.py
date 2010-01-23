# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from pressroom.register.forms import RegistrationForm

def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      return HttpResponse("Valid form!")
  else:
    form = RegistrationForm()
  
  return render_to_response('register/register.html', {'form':form})
  