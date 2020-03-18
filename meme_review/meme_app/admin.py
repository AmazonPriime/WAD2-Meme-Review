from django.contrib import admin
from meme_app.models import UserProfile, Meme, Comment, Category

admin.site.register(UserProfile)
admin.site.register(Meme)
admin.site.register(Comment)
admin.site.register(Category)
