import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','meme_review.settings')

import django
django.setup()
from meme_app.models import UserProfile,Category,Meme,Comment,User
import datetime



def populate():
	#Clearing the script each time its run
	Queryset = UserProfile.objects.all()
	Queryset1 = Meme.objects.all()
	Queryset2 = Comment.objects.all()
	Queryset3 = Category.objects.all()
	Queryset4 = User.objects.all()
	Queryset.delete()
	Queryset1.delete()
	Queryset2.delete()
	Queryset3.delete()
	Queryset4.delete()



	categories = ['Nature','Science','Games','Stories','Business','Celebrities','Design','Food and drink','Art','Gardening','Technology'] 
	users = [
	{'username':'Thomas','password':'admin','image':'profile_images/profile1.jfif','dob':'2000-11-11','bio':'Looking happy'},
	{'username':'Selim','password':'admin','image':'profile_images/me.jpg','dob':'1789-10-10','bio':'Looking into the distance'},
	{'username':'Amazon','password':'admin','image':'profile_images/profile3.jfif','dob':'1998-09-19','bio':'Blue shirt guy'},
	{'username':'Luke','password':'admin','image':'profile_images/profile2.jfif','dob':'1992-08-08','bio':'Looking happy'},
	{'username':'Matthew','password':'admin','image':'profile_images/profile4.jfif','dob':'1968-07-21','bio':'Person with umbrella'},
	{'username':'Adam','password':'admin','image':'profile_images/profile5.jfif','dob':'1984-06-27','bio':'Rain jacket guy'},
	{'username':'Lucy','password':'admin','image':'profile_images/profile6.jfif','dob':'1973-05-05','bio':'Curly haired with beard guy'},
	{'username':'Stephen','password':'admin','image':'profile_images/profile6.jfif','dob':'1961-04-14','bio':'Blue jacket girl'},
	]

	memes = [
	{'user':'Thomas','title':'Meme1','picture':'meme_images/onlinelectures.jpg','date':'2020-03-24','likes':'20','dislikes':'5','views':'500','category':'Science','nsfw':'False'},
	{'user':'Adam','title':'Meme2','picture':'meme_images/goingoutside.jpg','date':'2020-03-25','likes':'99999999','dislikes':'200','views':'349','category':'Business','nsfw':'True'},
	{'user':'Adam','title':'Meme3','picture':'meme_images/god.jpg','date':'2020-03-26','likes':'120','dislikes':'90','views':'487','category':'Games','nsfw':'False'},
	{'user':'Adam','title':'Meme4','picture':'meme_images/dogmeme.jpg','date':'2020-03-27','likes':'20','dislikes':'21','views':'604','category':'Gardening','nsfw':'True'},
	{'user':'Selim','title':'Meme5','picture':'meme_images/avacado.jpg','date':'2020-03-30','likes':'12','dislikes':'40','views':'215','category':'Art','nsfw':'False'},
	{'user':'Lucy','title':'Meme6','picture':'meme_images/meme1.jpg','date':'2020-03-30','likes':'98','dislikes':'23','views':'361','category':'Food and drink','nsfw':'False'},
	{'user':'Stephen','title':'Meme7','picture':'meme_images/meme2.jpg','date':'2020-03-30','likes':'88','dislikes':'57','views':'5766','category':'Design','nsfw':'False'},]

	comments = [
	{'user':'Matthew','title':'Meme1','text':'that kid who rickrolled everyone','date':'2020-03-24','likes':'3','dislikes':'2'},
	{'user':'Matthew','title':'Meme1','text':'But what does alt f4 do','date':'2020-03-25','likes':'2','dislikes':'2'},
	{'user':'Amazon','title':'Meme1','text':'The online gamer community, coming to a teaching chat near you!','date':'2020-03-27','likes':'3','dislikes':'3'},
	{'user':'Lucy','title':'Meme2','text':'Nice work but why dont people listen','date':'2020-03-26','likes':'7','dislikes':'16'},
	{'user':'Stephen','title':'Meme2','text':'First they said , I dare you, i double dare you. Now they are running behind me with their baton.','date':'2020-03-26','likes':'32','dislikes':'12'},
	{'user':'Amazon','title':'Meme2','text':'The government cant stop us from going outside','date':'2020-03-28','likes':'90','dislikes':'54'},
	{'user':'Selim','title':'Meme3','text':'God is holding the devils water.','date':'2020-03-26','likes':'45','dislikes':'0'},
	{'user':'Lucy','title':'Meme3','text':'This was a bizarre interview wasn’t it!','date':'2020-03-28','likes':'0','dislikes':'12'},
	{'user':'Thomas','title':'Meme3','text':'Thus a meme is born.','date':'2020-03-27','likes':'20','dislikes':'23'},
	{'user':'Matthew','title':'Meme4','text':'Mess with the pom, you get the nom','date':'2020-03-27','likes':'23','dislikes':'19'},
	{'user':'Lucy','title':'Meme4','text':'Hey dont forget doggo is love doggo is life','date':'2020-03-27','likes':'2','dislikes':'53'},
	{'user':'Thomas','title':'Meme4','text':'Mess with the retriever, you get the cleaver','date':'2020-03-29','likes':'23','dislikes':'41'},
	{'user':'Stephen','title':'Meme5','text':'The perfect avacado doesnt exist!','date':'2020-03-30','likes':'78','dislikes':'12'},
	{'user':'Amazon','title':'Meme5','text':'Game of thrones had such a bad ending','date':'2020-03-30','likes':'93','dislikes':'67'},
	{'user':'Selim','title':'Meme5','text':'How do you cut an avacado perfectly?','date':'2020-03-30','likes':'5','dislikes':'10'},
	]

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


	def add_meme(user,title,picture,date,likes,dislikes,views,category,nsfw):
		m = Meme.objects.get_or_create(user=user,title=title,picture=picture,date=date,likes=likes,dislikes=dislikes,views=views,category=category,nsfw=nsfw)[0]
		m.save()
		return m

	for meme in memes:
		username = meme['user']
		instanceuser = UserProfile.objects.get(user__username=username)
		category = meme['category']
		instancecategory = Category.objects.get(name=category)
		m = add_meme(instanceuser, meme['title'],meme['picture'],meme['date'],meme['likes'],meme['dislikes'],meme['views'],instancecategory,meme['nsfw'])


	def add_comment(user,meme,text,date,likes,dislikes):
		c = Comment.objects.get_or_create(user=user,meme=meme,text=text,date=date,likes=likes,dislikes=dislikes)[0]
		c.save()
		return c

	for comment in comments:
		username = comment['user']
		instanceuser = UserProfile.objects.get(user__username=username)
		meme = comment['title']
		instancetitle = Meme.objects.get(title=meme)
		c = add_comment(instanceuser,instancetitle,comment['text'],comment['date'],comment['likes'],comment['dislikes'])


if __name__ == '__main__':
	print('Starting Memez population script...')
	populate()
