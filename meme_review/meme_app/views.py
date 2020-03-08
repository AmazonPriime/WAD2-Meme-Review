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
