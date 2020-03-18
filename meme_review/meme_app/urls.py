from django.urls import path
from django.urls import include
from meme_app import views

app_name = 'meme_app'

urlpatterns = [
	path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('top_memes', views.top_memes, name='top_memes'),
    path('user_details', views.user_details, name='user_details'),
    path('account_home', views.account_home, name='account_home'),
    path('category', views.category, name='category'),
    path('meme', views.meme, name='meme'),
    path('meme_creator', views.meme_creator, name='meme_creator'),
]
