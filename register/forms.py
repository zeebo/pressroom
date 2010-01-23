from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
  email = forms.EmailField(label="Your E-Mail")
  first_name = forms.CharField(max_length=20, label="Your first name")
  last_name = forms.CharField(max_length=20, label="Your last name")
  password = forms.CharField(widget=forms.PasswordInput, label="Your Password")  
  
  def clean_email(self):
    data = self.cleaned_data['email']
    if data:
      if User.objects.filter(username=data).count() > 0:
        raise forms.ValidationError("Email already registered")
    
    return data