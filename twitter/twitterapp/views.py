import datetime
from django.shortcuts import render
from twitterapp.models import Tweet, User
from twitterapp.forms import TweetForm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def all_tweets(request):
    """Get all the tweets in the system.
    """
    tweets = Tweet.objects.all()
    tweet_form =  TweetForm()
    return render(request, 'twitterapp/detail.html', { 'tweets' : tweets, 'form': tweet_form })

def user_tweets(request,user_id):
    """Get all the tweets by the specific user as per their ID
    """
    tweets = Tweet.objects.filter(user__id=user_id)
    return render(request, 'twitterapp/user_tweets.html', { 'tweets' : tweets })

def new_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['tweet']
            t1 = Tweet.objects.create(
                content=content,
                date=datetime.datetime.now(),
                user=User.objects.get(id=1)
                )
            t1.save()
    return HttpResponseRedirect('/twitter/')          



