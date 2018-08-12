# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect
from.models import Post,Comment,ContactMe,Category

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-publish_datetime')
    pginator = Paginator(posts,6)
    page = request.GET.get('page')
    try:
        posts = pginator.page(page)
    except PageNotAnInteger:
        posts = pginator.page(1)
    except EmptyPage:
        posts = pginator.page(pginator.num_pages)
    context = {
        'posts':posts,
        'recent_post':posts[:5]
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == 'POST':
        this_name = request.POST['name']
        this_email = request.POST['email']
        this_url = request.POST['url']
        this_message = request.POST['message']

        ContactMe.objects.create(name=this_name,email=this_email,website=this_url,message=this_message)
        return HttpResponseRedirect('/contact/')


    return render(request,'contact.html')

def post(request,id):
    this_post = Post.objects.get(id=id)
    if request.method == 'POST':
        this_name = request.POST['name']
        this_email = request.POST['email']
        this_url = request.POST['url']
        this_message = request.POST['message']

        Comment.objects.create(name=this_name,email=this_email,website=this_url,text=this_message,for_post=this_post)
        return HttpResponseRedirect(redirect_to='/post/{}'.format(id))
    comments = Comment.objects.filter(for_post=this_post)
    context = {
        'post':this_post,
        'comments':comments,
        'comments_numb':int(len(comments))
    }
    return render(request,'post.html',context)

def categories_list(request):
    categories = Category.objects.all()
    context = {
        'categories':categories,
    }
    return render(request,'categories.html',context)

def categorypost(request,id):
    this_category = Category.objects.get(id=id)
    posts = Post.objects.filter(category=this_category)
    context = {
        'posts':posts,
    }
    return render(request,'index.html',context)