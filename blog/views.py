import random
from django.shortcuts import render

# Create your views here.
import random
from django.shortcuts import render

# 1. Data (same author – add your own text / image URLs)
BLOGS = [
   "My name is Kuany Chol Kuany Lueth, please correct that on your list. Thank you!",
    "I started coding with Python in 2025 and never looked back.",
    "Django makes web development so fast that I can focus on ideas.",
    "Teaching others to code is the best way to learn deeper.",
]

IMAGES = [
    "https://avatars.githubusercontent.com/u/583231?v=4",
    "https://django-project.com/s/img/logos/django-logo-negative.png",
    "https://picsum.photos/seed/python/500/300",
]

def blog(request):
    """Main page: one random blog + one random image"""
    context = {
        'blog_text': random.choice(BLOGS),
        'image_url': random.choice(IMAGES),
    }
    return render(request, 'blog/blog.html', context)

def show_all(request):
    """Show every blog and every image"""
    return render(request, 'blog/show_all.html',
                  {'blogs': BLOGS, 'images': IMAGES})

def about(request):
    """About me page"""
    return render(request, 'blog/about.html')
