from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import random
from DjangoApp.apps.rss_news.models import Post


# Create your views here.

def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'index.html', context)


def post(request, index):
    try:
        post = Post.objects.get(id=index)
    except Post.DoesNotExist:
        return HttpResponse('Post does not exist')

    context = {
        'post': post
    }

    return render(request, 'post.html', context)


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def signup_user(request):
    if request.POST:
        user_name = request.POST["user_name"]
        password = request.POST["password"]
        repeat_password = request.POST["repeat_password"]
        email = request.POST["email"]
        print(user_name, password, repeat_password, email)
        return HttpResponseRedirect('/')
    else:
        print("error page")


def check_user_name(request):
    if request.GET:
        user_name = request.GET["user_name"]

        names = ("Katya", "Igor", "Maxim", "Anna")

        if user_name in names:
            return HttpResponse("yes")
        else:
            return HttpResponse("no")

    else:
        pass