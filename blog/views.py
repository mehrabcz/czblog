# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from.models import Post,Comment
# Create your views here.

def index(request):
    posts = Post.objects.all()
    my_post = posts[0]
    comments = Comment.objects.filter(for_post=my_post)
    context = {
        'posts':posts,
        'comments':comments
    }
    return render(request,'index.html',context)