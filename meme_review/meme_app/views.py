from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'meme_app/index.html')

def login(request):
    return render(request, 'meme_app/login.html')

def register(request):
    return render(request, 'meme_app/register.html')
    
def top_memes(request):
    return render(request, 'meme_app/topmemes.html')

def user_details(request):
    return render(request, 'meme_app/userdetails.html')

def account_home(request):
    return render(request, 'meme_app/accounthome.html')
    
def category(request):
    return render(request, 'meme_app/category.html')

def meme(request):
    return render(request, 'meme_app/meme.html')
    
def meme_creator(request):
    return render(request, 'meme_app/memecreator.html')