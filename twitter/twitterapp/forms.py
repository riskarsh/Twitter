from django import forms

class TweetForm(forms.Form):
    tweet = forms.CharField(label='tweet', max_length=140)