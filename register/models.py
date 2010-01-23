from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RegistrationToken(models.Model):
  user = models.ForeignKey(User)
  token = models.CharField(max_length=50)
  reg_date = models.DateTimeField(auto_now_add=True)
