import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','meme_review.settings')

import django
django.setup()
from meme_app.models import UserProfile,Category,Meme,Comment,User
import datetime



def populate():
	categories = ['Nature','Science','Games','Stories','Business']
	users = [
	{'username':'Thomas','password':'admin','image':'profile_images/profile1.jfif','dob':'2000-11-11','bio':'Looking happy'},
	{'username':'Selim','password':'admin','image':'profile_images/profile2.jfif','dob':'1999-10-10','bio':'Looking into the distance'},
	{'username':'AmazonP','password':'admin','image':'profile_images/profile3.jfif','dob':'1998-09-09','bio':'Blue shirt guy'}]

	memes = [
	{'user':'Thomas','title':'Meme1','picture':'meme_images/meme1.jpg','date':'2020-03-11','likes':'20','dislikes':'5','category':'Science','nsfw':'False'},
	{'user':'Thomas','title':'Meme2','picture':'meme_images/meme2.jpg','date':'2020-03-11','likes':'5','dislikes':'200','category':'Business','nsfw':'True'},
	{'user':'Thomas','title':'Meme3','picture':'meme_images/meme3.jpg','date':'2020-03-11','likes':'120','dislikes':'90','category':'Games','nsfw':'False'}]

	comments = [
	{'user':'Thomas','title':'Meme1','text':'Text for meme 1','date':'2020-04-04','likes':'1','dislikes':'1'},
	{'user':'Selim','title':'Meme2','text':'Text for meme 2','date':'2020-05-05','likes':'2','dislikes':'2'},
	{'user':'AmazonP','title':'Meme3','text':'Text for meme 3','date':'2020-06-06','likes':'3','dislikes':'3'}]

	def add_cat(cat):
		c = Category.objects.get_or_create(name=cat)[0]
		c.save()
		return c

	def add_user(username, password, image, dob, bio):
		u = User.objects.get_or_create(username=username,password=password)[0]
		u.save()
		up = UserProfile.objects.get_or_create(user=u, picture=image, dob=dob, bio=bio)[0]
		up.save()
		return up

	for cat in categories:
		c = add_cat(cat)

	for user in users:
		u = add_user(user['username'], user['password'], user['image'], user['dob'], user['bio'])


	def add_meme(user,title,picture,date,likes,dislikes,category,nsfw):
		m = Meme.objects.get_or_create(user=user,title=title,picture=picture,date=date,likes=likes,dislikes=dislikes,category=category,nsfw=nsfw)[0]
		m.save()
		return m

	for meme in memes:
		username = meme['user']
		instanceuser = UserProfile.objects.get(user__username=username)
		category = meme['category']
		instancecategory = Category.objects.get(name=category)
		m = add_meme(instanceuser, meme['title'],meme['picture'],meme['date'],meme['likes'],meme['dislikes'],instancecategory,meme['nsfw'])


	def add_comment(user,meme,text,date,likes,dislikes):
		c = Comment.objects.get_or_create(user=user,meme=meme,text=text,date=date,likes=likes,dislikes=dislikes)[0]
		c.save()
		return c

	for comment in comments:
		username = comment['user']
		instanceuser = UserProfile.objects.get(user__username=username)
		#print(instanceuser, ":instanceuser")
		meme = comment['title']
		#print(meme ,":meme")
		instancetitle = Meme.objects.get(title=meme)
		#print(instancetitle, ":instancetitle")
		c = add_comment(instanceuser,instancetitle,comment['text'],comment['date'],comment['likes'],comment['dislikes'])


if __name__ == '__main__':
	print('Starting Memez population script...')
	populate()
