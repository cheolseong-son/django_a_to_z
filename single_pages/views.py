from django.shortcuts import render, redirect
from blog.models import Post
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def landing(request):
    recent_posts = Post.objects.order_by('-pk')[:3]
    return render(
        request,
        'single_pages/landing.html',
        {
            'recent_posts':recent_posts,
        }
    )

def about_me(request):
    return render(
        request,
        'single_pages/about_me.html'
    )

# Create your views here.
