from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns= [
    path('',views.all_tweets,name='all_tweets'),
    path('<int:user_id>/',views.user_tweets,name='user_tweets')

]