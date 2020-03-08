from django.urls import path
from django.urls import include
from meme_app import views

app_name = 'meme_app'

urlpatterns = [
	path('', views.index, name='index'),
        path('login', views.login, name='login'),
        path('register', views.register, name='register'),
        path('top_memes', views.top_memes, name='top_memes'),
]
