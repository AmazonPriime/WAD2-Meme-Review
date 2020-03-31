import os, datetime, django, random, uuid

os.environ.setdefault('DJANGO_SETTINGS_MODULE','meme_review.settings')
django.setup()

from meme_app.models import User, UserProfile, Category, Meme, Comment, CommentRating, MemeRating, View

# function to get and delete all records in the db
def clean():
	User.objects.all().delete()
	UserProfile.objects.all().delete()
	Meme.objects.all().delete()
	Comment.objects.all().delete()
	User.objects.all().delete()
	CommentRating.objects.all().delete()
	MemeRating.objects.all().delete()
	View.objects.all().delete()

# function to add a category to the database
def add_category(name):
	category = Category.objects.get_or_create(name = name)[0]
	category.save()

# function to add a user and userprofile to the databse
def add_user(username, password, image, dob, bio):
	user = User.objects.get_or_create(username = username, password = password)[0]
	user.save()
	user_profile = UserProfile.objects.get_or_create(user = user, picture = image, dob = dob, bio = bio)[0]
	user_profile.save()

# function to add a meme to the database
def add_meme(user, title, picture, date, category, nsfw):
	meme = Meme.objects.get_or_create(user = user, title = title, picture = picture, date = date, category = category, nsfw = nsfw)[0]
	meme.save()
	return meme

def add_meme_views(meme, views):
	for i in range(views):
		view = View.objects.get_or_create(viewer_id = uuid.uuid4(), meme = meme)[0]
		meme.views += 1
		view.save()
	meme.save()

# function to add a comment to the database
def add_comment(user, meme, text, date):
	comment = Comment.objects.get_or_create(user = user, meme = meme, text = text, date = date)[0]
	comment.save()

# function to add a like to a meme
def add_meme_rating(user, meme, value):
	meme_rating = MemeRating.objects.get_or_create(user = user, meme = meme, value = value)[0]
	if value == 1:
		meme.likes += 1
	else:
		meme.dislikes += 1
	meme.save()
	meme_rating.save()

# function to add a like to a comment
def add_comment_rating(user, comment, value):
	comment_rating = CommentRating.objects.get_or_create(user = user, comment = comment, value = value)[0]
	if value == 1:
		comment.likes += 1
	else:
		comment.dislikes += 1
	comment.save()
	comment_rating.save()

def populate():
	categories = ['Nature', 'Science', 'Games', 'Stories', 'Business', 'Celebrities', 'Design', 'Food and drink', 'Art', 'Gardening', 'Technology', 'Misc']

	users = [
		{'username':'Thomas', 'password':'password', 'image':'profile_images/profile1.jfif', 'dob':'2000-11-11', 'bio':'Looking happy'},
		{'username':'Selim', 'password':'password', 'image':'profile_images/me.jpg', 'dob':'1789-10-10', 'bio':'Looking into the distance'},
		{'username':'Amazon', 'password':'password', 'image':'profile_images/profile3.jfif', 'dob':'1998-09-19', 'bio':'Blue shirt guy'},
		{'username':'Luke', 'password':'password', 'image':'profile_images/profile2.jfif', 'dob':'1992-08-08', 'bio':'Looking happy'},
		{'username':'Matthew', 'password':'password', 'image':'profile_images/profile4.jfif', 'dob':'1968-07-21', 'bio':'Person with umbrella'},
		{'username':'Adam', 'password':'password', 'image':'profile_images/profile5.jfif', 'dob':'1984-06-27', 'bio':'Rain jacket guy'},
		{'username':'Lucy', 'password':'password', 'image':'profile_images/profile6.jfif', 'dob':'1973-05-05', 'bio':'Curly haired with beard guy'},
		{'username':'Stephen', 'password':'password', 'image':'profile_images/profile6.jfif', 'dob':'1961-04-14', 'bio':'Blue jacket girl'},
	]

	memes = [
		{'user':'Thomas', 'title':'Boomer Zoomers', 'picture':'meme_images/onlinelectures.jpg', 'date':'2020-03-24', 'views':'12', 'category':'Science', 'nsfw':'False'},
		{'user':'Adam', 'title':'Lockdown', 'picture':'meme_images/goingoutside.jpg', 'date':'2020-03-25', 'views':'4', 'category':'Business', 'nsfw':'True'},
		{'user':'Adam', 'title':'Uh-oh', 'picture':'meme_images/god.jpg', 'date':'2020-03-26', 'views':'15', 'category':'Games', 'nsfw':'False'},
		{'user':'Adam', 'title':'He protec, he attac', 'picture':'meme_images/dogmeme.jpg', 'date':'2020-03-27', 'views':'0', 'category':'Gardening', 'nsfw':'True'},
		{'user':'Selim', 'title':'Queen of Avocados', 'picture':'meme_images/avacado.jpg', 'date':'2020-03-30', 'views':'6', 'category':'Art', 'nsfw':'False'},
		{'user':'Lucy', 'title':'Sean "Baked" Beans', 'picture':'meme_images/meme1.jpg', 'date':'2020-03-30', 'views':'22', 'category':'Food and drink', 'nsfw':'False'},
		{'user':'Stephen', 'title':'Realisation', 'picture':'meme_images/meme2.jpg', 'date':'2020-03-30', 'views':'9', 'category':'Design', 'nsfw':'False'},
		{'user':'Thomas', 'title':'Chinas infection rate', 'picture':'meme_images/china.jpg', 'date':'2020-03-31', 'views':'9', 'category':'Misc', 'nsfw':'False'},
		{'user':'Adam', 'title':'Satan killing spree', 'picture':'meme_images/corona.jpg', 'date':'2020-03-31', 'views':'12', 'category':'Misc', 'nsfw':'False'},
		{'user':'Adam', 'title':'Comedy gold', 'picture':'meme_images/generations.jpg', 'date':'2020-03-31', 'views':'2', 'category':'Misc', 'nsfw':'False'},
		{'user':'Adam', 'title':'You guys have different ones?', 'picture':'meme_images/language.png', 'date':'2020-03-31', 'views':'6', 'category':'Misc', 'nsfw':'False'},
		{'user':'Selim', 'title':'We have no infections!', 'picture':'meme_images/northkorea.jpg', 'date':'2020-03-31', 'views':'10', 'category':'Misc', 'nsfw':'False'},
		{'user':'Lucy', 'title':'Drop drop it', 'picture':'meme_images/prison.jpg', 'date':'2020-03-31', 'views':'9', 'category':'Misc', 'nsfw':'False'},
		{'user':'Stephen', 'title':'I knew there was something up with her', 'picture':'meme_images/queen.jpg', 'date':'2020-03-31', 'views':'5', 'category':'Misc', 'nsfw':'False'},
		{'user':'Amazon', 'title':'Toaster better than girlfriend 100% proven', 'picture':'meme_images/toasterwin.jpg', 'date':'2020-03-31', 'views':'22', 'category':'Misc', 'nsfw':'False'},
		{'user':'Amazon', 'title':'Ahh that\'s hot!', 'picture':'meme_images/witcher.jpg', 'date':'2020-03-31', 'views':'9', 'category':'Misc', 'nsfw':'False'},
		{'user':'Amazon', 'title':'Working at home be like', 'picture':'meme_images/workfromhome.jpg', 'date':'2020-03-31', 'views':'30', 'category':'Misc', 'nsfw':'False'},
	]

	comments = [
		{'user':'Matthew', 'title':'Boomer Zoomers', 'text':'that kid who rickrolled everyone', 'date':'2020-03-24'},
		{'user':'Matthew', 'title':'Boomer Zoomers', 'text':'But what does alt f4 do', 'date':'2020-03-25'},
		{'user':'Amazon', 'title':'Boomer Zoomers', 'text':'The online gamer community,  coming to a teaching chat near you!', 'date':'2020-03-27'},
		{'user':'Lucy', 'title':'Lockdown', 'text':'Nice work but why dont people listen', 'date':'2020-03-26'},
		{'user':'Stephen', 'title':'Lockdown', 'text':'First they said, I dare you,  i double dare you. Now they are running behind me with their baton.', 'date':'2020-03-26'},
		{'user':'Amazon', 'title':'Lockdown', 'text':'The government cant stop us from going outside', 'date':'2020-03-28'},
		{'user':'Selim', 'title':'Uh-oh', 'text':'God is holding the devils water.', 'date':'2020-03-26'},
		{'user':'Lucy', 'title':'Uh-oh', 'text':'This was a bizarre interview wasn’t it!', 'date':'2020-03-28'},
		{'user':'Thomas', 'title':'Uh-oh', 'text':'Thus a meme is born.', 'date':'2020-03-27'},
		{'user':'Matthew', 'title':'He protec, he attac', 'text':'Mess with the pom, you get the nom', 'date':'2020-03-27'},
		{'user':'Lucy', 'title':'He protec, he attac', 'text':'Hey dont forget doggo is love doggo is life', 'date':'2020-03-27'},
		{'user':'Thomas', 'title':'He protec, he attac', 'text':'Mess with the retriever, you get the cleaver', 'date':'2020-03-29'},
		{'user':'Stephen', 'title':'Queen of Avocados', 'text':'The perfect avacado doesnt exist!', 'date':'2020-03-30'},
		{'user':'Amazon', 'title':'Queen of Avocados', 'text':'Game of thrones had such a bad ending', 'date':'2020-03-30'},
		{'user':'Selim', 'title':'Queen of Avocados', 'text':'How do you cut an avacado perfectly?', 'date':'2020-03-30'},
	]

	print("> Adding categories")
	for category in categories:
		add_category(category)
		print(f">> Added {category}")

	print()

	print("> Adding users")
	for user in users:
		add_user(user['username'], user['password'], user['image'], user['dob'], user['bio'])
		print(f">> Added {user['username']}")

	print()

	print("> Adding memes")
	for meme in memes:
		user_profile = UserProfile.objects.get(user__username = meme['user'])
		category = Category.objects.get(name = meme['category'])
		views = int(meme['views'])
		meme = add_meme(user_profile, meme['title'], meme['picture'], meme['date'], category, meme['nsfw'])
		add_meme_views(meme, views)
		print(f">> Added {meme.title}")

	print()

	print("> Adding comments")
	for comment in comments:
		user = UserProfile.objects.get(user__username = comment['user'])
		meme = Meme.objects.get(title = comment['title'])
		add_comment(user, meme, comment['text'], comment['date'])
		print(f">> Added {comment['user']}: {comment['text']}")

	print()

	print("> Adding meme ratings")
	while memes:
		meme = memes.pop(random.randint(0, len(memes) - 1))
		meme = Meme.objects.get(title = meme['title'])
		for user in users[random.randint(0, len(users) - 1) : len(users) - 1]:
			user = UserProfile.objects.get(user__username = user['username'])
			value = 1 if random.randint(0, 1) == 1 else -1
			add_meme_rating(user, meme, value)
			print(f">> Added {user.user.username}", ('liked' if value == 1 else 'disliked'), f'"{meme.title}"')

	print()

	print("> Adding comment ratings")
	while comments:
		comment = comments.pop(random.randint(0, len(comments) - 1))
		comment = Comment.objects.get(text = comment['text'])
		for user in users[random.randint(0, len(users) - 1) : len(users) - 1]:
			user = UserProfile.objects.get(user__username = user['username'])
			value = 1 if random.randint(0, 1) == 1 else -1
			add_comment_rating(user, comment, value)
			print(f">> Added {user.user.username}", ('liked' if value == 1 else 'disliked'), f'"{comment.text}"')

if __name__ == '__main__':
	print('Starting Memez population script...')
	clean()
	print('> Cleaned old database records.')
	populate()
	print('> All records added.')
	print('~~ Fin.')
