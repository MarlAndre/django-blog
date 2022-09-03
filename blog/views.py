from datetime import date

from django.shortcuts import render

from .models import Post

all_posts = [

]

def get_date(post):
  return post['date']
# Create your views here.

def starting_page(request):
  latest_posts = Post.objects.all().order_by("-date")[:3] # last post created will be on top
  return render(request, "blog/index.html", { "posts": latest_posts})

def posts(request):
  return render(request, "blog/all-posts.html")

def post_detail(request, slug):
  return render(request, "blog/post-detail.html")