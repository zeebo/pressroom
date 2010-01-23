from django import forms

class RegistrationForm(forms.Form):
  email = forms.EmailField(label="Your E-Mail")
  password = forms.CharField(widget=forms.PasswordInput, label="Your Password")
  first_name = forms.CharField(max_length=20, label="Your first name")
  last_name = forms.CharField(max_length=20, label="Your last name")