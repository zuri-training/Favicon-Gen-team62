import email
from unicodedata import name
from django.db import models
from django.forms import modelform_factory

# Create your models here.
class User(models.Model) :
   user_id = models.serial
   first_name = models.CharField(max_length=100)
   last_name = models.CharField(max_length=100)
   email = models.CharField(max_length=100) 

class Avatar(models.Model) :
    user_id = models.serial
    avatar_id = models.int