from django.urls import path, re_path
from django.urls import include
from meme_app import views

app_name = 'meme_app'

urlpatterns = [
	path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('top_memes', views.top_memes, name='top_memes'),
    re_path(r'^user_details/(?P<username>.*)/$', views.user_details, name='user_details'),
    re_path(r'^account_home/(?P<username>.*)/$', views.account_home, name='account_home'),
    path('category', views.category, name='category'),
    path('meme', views.meme, name='meme'),
    path('meme_creator', views.meme_creator, name='meme_creator'),
]
