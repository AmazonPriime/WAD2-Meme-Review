from django.urls import path
from django.urls import include
from meme_app import views

app_name = 'meme_app'

urlpatterns = [
	path('', views.index, name='index'),
]
