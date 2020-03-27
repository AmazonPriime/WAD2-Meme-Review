import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','meme_review.settings')

import django
django.setup()
from meme_app.models import UserProfile,Category,Meme,Comment,User


def populate():
	categories = ['Nature','Science','Games','Stories','Business']
	users = [{'username':'Thomas','password':'admin'},{'username':'Selim','password':'admin'},{'username':'Amazon','password':'admin'}]

	def add_cat(cat):
		print(cat)
		p = Category.objects.get_or_create(name=cat)[0]
		p.save()
		return p

	for cat in categories:
		c = add_cat(cat)

	def add_user(username,password):
		print(username,password)
		u = User.objects.get_or_create(username=username,password=password)[0]
		u.save()
		return u

	for user in users:
		u = add_user(user['username'],user['password'])
	        
if __name__ == '__main__':
	print('Starting Memez population script...')
	populate()