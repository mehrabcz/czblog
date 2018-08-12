# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
# Create your models here.

    
class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    picture = models.ImageField(upload_to='category/%y/%m/%d/')

    def __unicode__(self):
        return self.name


class Post(models.Model):
    owner = models.ForeignKey(to=User)
    title = models.CharField(max_length=120)
    picture = models.ImageField(upload_to='posts/%y/%m/%d/')
    content = models.TextField()
    publish_datetime = models.DateTimeField(auto_now=False,auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True,auto_now_add=False)
    category = models.ForeignKey(to=Category,default=2)

class Comment(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    website = models.URLField()
    text  = models.TextField()
    for_post = models.ForeignKey(to=Post)
    publish_time = models.DateTimeField(auto_now=False,auto_now_add=True)

class ContactMe(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    website = models.URLField(null=True,blank=True)
    message = models.TextField()

