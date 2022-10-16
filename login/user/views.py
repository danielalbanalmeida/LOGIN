from django.shortcuts import render
from .models import *

def feed (request):
    posts = Post.objects.all()

    context = {'posts':posts}
    return render (request, 'social/feed.html')
# Create your views here.
