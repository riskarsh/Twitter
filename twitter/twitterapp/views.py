from django.shortcuts import render
from twitterapp.models import Tweet
from django.http import HttpResponse

# Create your views here.
def all_tweets(request):
    tweets = Tweet.objects.all()
    output = ""
    for tweet in tweets:
        output += "[{}] @{} - {}\n".format(tweet.date,tweet.user.name,tweet.content)
    return HttpResponse(output)

def user_tweets(request,user_id):
    tweets = Tweet.objects.filter(user__id=user_id)
    output = ""
    for tweet in tweets:
        output += "@{} - {} ".format(tweet.user.name,tweet.content)
    return HttpResponse(output)    