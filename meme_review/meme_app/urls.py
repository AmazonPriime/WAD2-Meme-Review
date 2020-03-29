from django.urls import path, re_path
from django.urls import include
from meme_app import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
	path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
	path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('top_memes/', views.top_memes, name='top_memes'),
    re_path(r'^account/(?P<username>.*)/$', views.account, name='account'),
    re_path(r'^category/(?P<cat>.*)/$', views.category, name='category'),
    re_path(r'^meme/(?P<id>.*)/$', views.meme, name='meme'),
	re_path(r'^rate/(?P<type>.*)/(?P<id>.*)/$', views.rate, name='rate'),
    path('meme_creator/', views.meme_creator, name='meme_creator'),
    path('about/', views.about, name='about'),
    path('unsupported/', views.unsupported, name='unsupported'),
    path('reset-password/', PasswordResetView.as_view(), name='password_reset'),
    path('reset-password/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset-password/confirm/<uidb64>[0-9A-Za-z]+)-<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
