from django.db import models
from django.db.models.base import Model

# Create your models here.
class User(models.Model):
    """User represents an account in our system.

    A user is an owner of the tweets in the system and is considered
    as the author. Each person who signs up has a corresponding 
    User in the database.
    """
    name = models.CharField(max_length=50)
    joined_date = models.DateTimeField('Account creation date')

class Tweet(models.Model):
    """Tweet represents a tweet and its metadata in our system.
    A tweet is a post that can be upto 140 characters long.
    """
    content = models.CharField(max_length=140)
    date = models.DateTimeField('Tweet date')
    user = models.ForeignKey(User, on_delete=models.CASCADE)