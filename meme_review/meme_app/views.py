from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from meme_app.models import Meme, UserProfile, Category, Comment
from meme_app.forms import UserForm, UserProfileForm, MemeForm
from datetime import datetime, timedelta, date
from django.core.paginator import Paginator
import random

def index(request):
    context_dict = {}
    memes = Meme.objects.all()

    # get a trending meme, random from 5 most liked in past week
    seven_days_ago = datetime.now() - timedelta(days = 7)
    recent_top_memes = memes.filter(date__range = [seven_days_ago, datetime.now()]).order_by('-likes')[:5]
    if(len(memes)>0):
        context_dict['trending_meme'] = memes[random.randint(0,len(memes) - 1)]
    else:
        context_dict['trending_meme'] = [] #pls fix this

    # get memes to store on popular today, top up to 9 memes from today
    yesterday = datetime.now() - timedelta(days = 1)
    context_dict['popular_memes'] = memes.filter(date__range = [yesterday, datetime.now()]).order_by('-likes')[:9]

    return render(request, 'meme_app/index.html', context_dict)

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            print('im doin it')
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username = username, password = password)
            if user:
                login(request, user)
                return redirect(reverse('index'))
            else:
                print(f"Invalid login details: {username}, {password}")
                return HttpResponse("Invalid login details supplied.")
        else:
            return render(request, 'meme_app/login.html')
    else:
        return redirect(reverse('index'))

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
            'registered' : registered
        }
        return render(request, 'meme_app/register.html', context_dict)
    else:
        return redirect(reverse('index'))

def top_memes(request):
    context_dict = {}
    memes = Meme.objects.all()

    # gets the top 9 memes of all time
    context_dict['top_memes'] = memes.order_by('-likes')[:9]

    return render(request, 'meme_app/topmemes.html', context_dict)

# ONE OF THESE TO BE REMOVED
def user_details(request, username):
    context_dict = {}
    try:
        # get the user and store in context dictionary
        user = UserProfile.objects.get(username = username)
        context_dict['user'] = user

        # get the user's memes and store them in the context dictionary
        memes = Meme.objects.all.filter(user = user)
        context_dict['memes'] = memes
    except:
        return render(request, '404.html')
    return render(request, 'meme_app/userdetails.html', context_dict)

def account_home(request, username):
    context_dict = {}
    try:
        # get the user and store in context dictionary
        user = UserProfile.objects.get(username = username)
        context_dict['user'] = user

        # get the user's memes and store them in the context dictionary
        memes = Meme.objects.all.filter(user = user)
        context_dict['memes'] = memes
    except:
        return render(request, '404.html')
    return render(request, 'meme_app/accounthome.html', context_dict)
############################

def category(request, cat):
    context_dict = {}
    # checks if the category exists
    try:
        cat_obj = Category.objects.all.get(name = cat)
    except:
        return render(request, '404.html')

    # gets memes with a specific category
    memes = Meme.objects.all.filter(category = cat_obj)
    paginator = Paginator(memes, 9) # 9 meme per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context_dict['page'] = page_obj
    context_dict['category'] = cat
    return render(request, 'meme_app/category.html', context_dict)

def meme(request, id):
    context_dict = {}
    # try and store meme in context dictionary
    try:
        context_dict['meme'] = Meme.objects.get(id = id)
        context_dict['comments'] = Comment.objects.all.filter(meme = context_dict['meme'])
    except:
        return render(request, '404.html')
    return render(request, 'meme_app/meme.html', context_dict)

#@login_required(login_url='login')
def meme_creator(request):
    if request.method == 'POST':
        meme_form = MemeForm(request.POST)

        if meme_form.is_valid():
            meme = meme_form.save(commit = False)
            meme.user = request.user
            meme.picture = request.FILES['picture']
            meme.save()
            return redirect(reverse('meme', args = [meme.id]))
        else:
            print(meme_form.errors)
    else:
        meme_form = MemeForm()


    context_dict = {'meme_form' : meme_form}
    return render(request, 'meme_app/memecreator.html', context_dict)

def about(request):
    return render(request,'meme_app/about.html')
