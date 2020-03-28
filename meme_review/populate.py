import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','meme_review.settings')

import django
django.setup()
from meme_app.models import UserProfile,Category,Meme,Comment,User


def populate():
	user_list = []
	category_list = []
	categories = ['Nature','Science','Games','Stories','Business']
	users = [
	{'username':'Thomas','password':'admin','image':'profile_images/profile1','dob':'2000-11-11','bio':'Girl Looking happy'},
	{'username':'Selim','password':'admin','image':'profile_images/profile2','dob':'1999-10-10','bio':'Looking into the distance'},
	{'username':'Amazon','password':'admin','image':'profile_images/profile3','dob':'1998-9-9','bio':'Blue shirt guy'}]

	def add_cat(cat):
		#print(cat)
		c = Category.objects.get_or_create(name=cat)[0]
		c.save()
		category_list.append(c)
		return c

	for cat in categories:
		c = add_cat(cat)

	def add_user(username,password,image,dob,bio):
		#print(username,password)
		u = User.objects.get_or_create(username=username,password=password)[0]
		u.save()
		user_list.append(u)
		up = UserProfile.objects.get_or_create(user=u,picture=image,dob=dob,bio=bio)[0]
		up.save()
		return up

	for user in users:
		u = add_user(user['username'],user['password'],user['image'],user['dob'],user['bio'])
	        
if __name__ == '__main__':
	print('Starting Memez population script...')
	populate()