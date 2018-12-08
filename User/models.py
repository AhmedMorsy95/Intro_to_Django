from django.db import models
import datetime

# Create your models here.

class User(models.Model):
    username  = models.CharField(max_length = 50)
    password  = models.CharField(max_length = 50)
    email  = models.CharField(max_length = 50)
    creationDate = models.DateField('Date', default=datetime.date.today)
