from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from meme_app.models import Meme, UserProfile, Category, Comment, View, MemeRating, CommentRating
from meme_app.forms import UserForm, UserProfileForm, MemeForm, AccountForm, CommentForm
from datetime import datetime, timedelta, date
from django.core.paginator import Paginator
from django.conf import settings
import random, re, base64, os

"""
Index View
returns:
    one of 5 top memes from the past 7 days
    top (up to 9) memes from within the last 24 hours
"""
def index(request):
    context_dict = {}
    memes = Meme.objects.all().filter(nsfw = (not restrictor(request.user))).order_by('-likes')
    context_dict['categories'] = Category.objects.all()

    # get a trending meme, random from 5 most liked in past week
    seven_days_ago = datetime.now() - timedelta(days = 7)
    recent_top_memes = memes.filter(date__range = [seven_days_ago, datetime.now()])[:5]
    if(len(memes)>0):
        context_dict['trending_meme'] = recent_top_memes[random.randint(0,len(recent_top_memes) - 1)]
    else:
        context_dict['trending_meme'] = None

    # get memes to store on popular today, top up to 9 memes from today
    yesterday = datetime.now() - timedelta(days = 1)
    context_dict['popular_memes'] = memes.filter(date__range = [yesterday, datetime.now()]).order_by('-likes')[:9]

    return render(request, 'meme_app/index.html', context_dict)

"""
User Login View
handles the login of a user
    if the login is successful it redurects them to the index page
    otherwise it will go back to the login page advising user that username/password is incorrect
"""
def user_login(request):
    context_dict = {}
    context_dict['categories'] = Category.objects.all()
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username = username, password = password)
            if user:
                login(request, user)
                return redirect(reverse('index'))
            else:
                messages.error(request, "Username or password is incorrect")
                return redirect(reverse('login'))
        else:
            return render(request, 'meme_app/login.html', context_dict)
    else:
        return redirect(reverse('index'))

"""
Logout View
simply logs the user out and redirects them to the index page
"""
@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect(reverse('index'))

"""
Registration View
handles the registration of a user
    if there the POST method is used it'll check the forms
    if the forms are valid it'll save the users details to the database
    if they're not valid the user is shown what the issues are in the form
"""
def register(request):
    if not request.user.is_authenticated:
        registered = False

        if request.method == 'POST':
            user_form = UserForm(request.POST)
            profile_form = UserProfileForm(request.POST)

            if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()
                profile = profile_form.save(commit = False)
                profile.user = user
                profile.save()
                registered = True
            else:
                print(user_form.errors, profile_form.errors)
        else:
            user_form = UserForm()
            profile_form = UserProfileForm()

        context_dict = {
            'user_form' : user_form,
            'profile_form' : profile_form,
            'registered' : registered,
            'categories' : Category.objects.all()
        }
        return render(request, 'meme_app/register.html', context_dict)
    else:
        return redirect(reverse('index'))

"""
Top Memes View
shows the top memes on the site including the top from the different categories
returns:
    the top 9 memes of all time
    the top 3 memes from each category
"""
def top_memes(request):
    context_dict = {}
    memes = Meme.objects.all().filter(nsfw = (not restrictor(request.user)))
    context_dict['categories'] = Category.objects.all()

    # gets the top 9 memes of all time
    context_dict['top_memes'] = {'Popular Memes' : memes.order_by('-likes')[:9]}

    # get the top 9 memes from each category
    for category in context_dict['categories']:
        context_dict['top_memes'][category.name] = [meme for meme in memes.filter(category = category).order_by('-likes')[:3]]

    return render(request, 'meme_app/topmemes.html', context_dict)

"""
Account View
handles the viewing of accounts and also allows a logged in user to edit their own account
    if the user is logged into their own account a form will be shown allowing them to edit their details
        if the request is POST and the forms are valid the details are saved and updated
    otherwise no form is shown
returns:
    memes from the user who's account is being viewed
        if the logged in user is viewing their own account the nsfw filter is not applied
    total meme count
    total amount of likes recieved
    total amount of dislikes recieved
"""
def account(request, username):
    context_dict = {}
    context_dict['categories'] = Category.objects.all()
    try:
        user = UserProfile.objects.get(user__username = username)
        context_dict['profile'] = user
    except:
        return render(request, '404.html', context_dict)

    memes = Meme.objects.all().filter(user = user)
    context_dict['meme_total'] = len(memes)
    context_dict['likes_total'] = sum([meme.likes for meme in memes])
    context_dict['dislikes_total'] = sum([meme.dislikes for meme in memes])

    if not request.user.username == username:
        memes = memes.filter(nsfw = (not restrictor(request.user)))

    context_dict['memes'] = memes

    if request.user.username == username:
        if request.method == 'POST':
            profile_form = AccountForm(request.POST)
            if profile_form.is_valid():
                user.bio = request.POST.get('bio')
                if 'picture' in request.FILES:
                    user.picture = request.FILES['picture']
                user.save()
            else:
                print(profile_form.errors)

        context_dict['profile_form'] = AccountForm(instance = user)

    # using this because had issues using user.picture as it would keep returning blank in the template
    context_dict['img_url'] = user.picture
    return render(request, 'meme_app/account.html', context_dict)

"""
Category View
handles the category pages including the pagnation of pages when theres more than 9 memes
returns:
    boolean for if there are any memes in this category
    page containing memes
    the category of the page
"""
def category(request, cat):
    context_dict = {}
    context_dict['categories'] = Category.objects.all()
    # checks if the category exists
    try:
        cat_obj = Category.objects.get(name = cat)
    except:
        return render(request, '404.html', context_dict)

    # gets memes with a specific category
    memes = Meme.objects.all().filter(category = cat_obj, nsfw = (not restrictor(request.user)))
    if not memes:
        context_dict['has_memes'] = False
    else:
        context_dict['has_memes'] = True

    # shows 9 memes per pagnator page
    paginator = Paginator(memes, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context_dict['page'] = page_obj
    context_dict['category'] = cat

    return render(request, 'meme_app/category.html', context_dict)

"""
Meme View
handles how the meme page is shown
retrieves and shows the meme to the user, also increments the view counter for the meme if the session id cannot be found in View table
if the user is logged in it'll also show the CommentForm so they can comment on a meme
returns:
    the meme to be displayed
    the comments for that meme
    the CommentForm - if the user is logged in
"""
def meme(request, id):
    context_dict = {}
    context_dict['categories'] = Category.objects.all()
    # try and store meme in context dictionary
    try:
        meme = Meme.objects.get(id = id)
        context_dict['meme'] = meme
        context_dict['comments'] = Comment.objects.all().filter(meme = context_dict['meme'])
        # check user session id and add the view to the meme
        if not request.session.session_key:
            request.session.save()
        key = request.session.session_key
        views = View.objects.filter(meme = meme, viewer_id = key)
        if not views:
            views = View(viewer_id = key, meme = meme)
            views.save()
            meme.views += 1
            meme.save()
    except:
        return render(request, '404.html', context_dict)

    if request.user.is_authenticated:
        context_dict['comment_form'] = CommentForm()

    return render(request, 'meme_app/meme.html', context_dict)

"""
Meme Creator View
handles the creation of memes
if the request is a post request the form is checked if valid
    when valid it creates a new meme object and stores the required data
    for the meme image since the byte data is sent over a helper function converts that to an image
    if the helper method returns -1 then the meme is deleted and user is sent back to the form with an error message
    otherwise the picture is saved to the server and url is saved on the model
returns:
    meme form so the user can put the details in for their meme
"""
@login_required(login_url='login')
def meme_creator(request):
    if request.method == 'POST':
        meme_form = MemeForm(request.POST)
        if meme_form.is_valid():
            meme = meme_form.save(commit = False)
            meme.user = UserProfile.objects.get(user = request.user)
            meme.save()
            meme_uri = meme_image(request.POST.get('picture'), meme.id)
            if meme_uri == -1:
                print("Image is invalid.")
                meme.delete()
                meme.save()
                return render(request, 'meme_app/memecreator.html', {'meme_form' : MemeForm(), 'categories' : Category.objects.all()})
            meme.picture = meme_uri
            meme.save()
            return redirect(reverse('meme', args = [meme.id]))
        else:
            print(meme_form.errors)
    else:
        meme_form = MemeForm()

    context_dict = {'meme_form' : meme_form, 'categories' : Category.objects.all()}
    return render(request, 'meme_app/memecreator.html', context_dict)

# meme_creator helper method
def meme_image(dataURL, id):
    dataUrlPattern = re.compile('data:image/(png|jpeg);base64,(.*)$')
    image_data = dataUrlPattern.match(dataURL).group(2)
    if image_data == None or len(image_data) == 0:
        return -1
    image_data = base64.b64decode(image_data)
    filepath = os.path.join(settings.MEDIA_ROOT, 'meme_images', f"{id}.png")
    with open(filepath, 'wb') as f:
        f.write(image_data)
    return os.path.join('meme_images', f"{id}.png")

"""
Comment View
handles the commenting on a meme
if the request is a POST request the form is checked to be valid
    if it's invalid the user is sent back with an error message
    otherwise the data is stored in the database and use is returned to the meme they commented on
"""
@login_required(login_url='login')
def comment(request, id):
    try:
        meme = Meme.objects.get(id = id)
    except:
        return render(request, '404.html', {'categories' : Category.objects.all()})

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit = False)
            comment.user = UserProfile.objects.get(user = request.user)
            comment.meme = meme
            comment.save()
        else:
            print(comment_form.errors)

    return redirect(reverse('meme', args = [meme.id]))

"""
About View
simply returns the about page
"""
def about(request):
    context_dict = {}
    context_dict['categories'] = Category.objects.all()
    return render(request,'meme_app/about.html', context_dict)

"""
Unsupported View
simply returns the unsupported browser page
"""
def unsupported(request):
    return render(request,'unsupported.html')

"""
Rate View
handles how ratings are applied to both memes and comments
depending on whether type is meme or comment the MemeRating or CommentRating is created
the helper method do_rating makes sure that previous like/dislike is handled correctly
    if the user has liked or disliked before it removes the rating and applies the new one
    if they have never rated it just applies it
"""
@login_required(login_url='login')
def rate(request, id, type):
    context_dict = {}
    context_dict['categories'] = Category.objects.all()

    try:
        value = int(request.GET.get('value'))
        user = UserProfile.objects.get(user = request.user)
        if type == "meme":
            meme = Meme.objects.get(id = id)
            rating = MemeRating.objects.get_or_create(meme = meme, user = user)[0]
            do_rating(meme, rating, value)
            meme.save()
            rating.save()
            return redirect(reverse('meme', args = [meme.id]))

        elif type == "comment":
            comment = Comment.objects.get(id = id)
            rating = CommentRating.objects.get_or_create(comment = comment, user = user)[0]
            do_rating(comment, rating, value)
            comment.save()
            rating.save()
            return redirect(reverse('meme', args = [comment.meme.id]))

        else:
            return render(request, '404.html', context_dict)
    except:
        return render(request, '404.html', context_dict)

# helper methods for the rate view
def do_rating(model, rating, value):
    if rating.value == 0:
        # no prev rating
        rating.value = value
        if value == 1:
            model.likes += 1
        elif value == -1:
            model.dislikes += 1

    elif rating.value == 1:
        # prev rating was a like
        if value == -1:
            rating.value = value
            model.likes -= 1
            model.dislikes += 1

    elif rating.value == -1:
        # prev rating was a dislike
        if value == 1:
            rating.value = value
            model.likes += 1
            model.dislikes -= 1

# helper method to make sure user is able to see NSFW memes
def restrictor(user):
    if not user.is_authenticated:
        return True
    else:
        try:
            user = UserProfile.objects.get(user__username == user.username)
            age_years = (date.today() - user.dob).days / 365.25
            if age_years > 18:
                return False
            else:
                return True
        except:
            return True
