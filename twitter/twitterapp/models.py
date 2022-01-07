from django.db import models
from django.db.models.base import Model

# Create your models here.
class User(models.Model): 
    name = models.CharField(max_length=50)
    joined_date = models.DateTimeField('Acc creation date')

class Tweet(models.Model):
    content = models.CharField(max_length=140)
    date = models.DateTimeField('Tweet date')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
