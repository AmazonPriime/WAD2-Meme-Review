from django.urls import path, re_path
from django.urls import include
from meme_app import views

urlpatterns = [
	path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('top_memes/', views.top_memes, name='top_memes'),
    re_path(r'^user_details/(?P<username>.*)/$', views.user_details, name='user_details'),
    re_path(r'^account_home/(?P<username>.*)/$', views.account_home, name='account_home'),
    re_path(r'^category/(?P<cat>.*)/$', views.category, name='category'),
    re_path(r'^meme/(?P<id>.*)/$', views.meme, name='meme'),
    path('meme_creator/', views.meme_creator, name='meme_creator'),
    path('about/', views.about, name='about'),
]
