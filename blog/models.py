# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    owner = models.ForeignKey(to=User)
    title = models.CharField(max_length=120)
    picture = models.ImageField(upload_to='posts/%y/5m/%d')
    content = models.TextField()

class Comment(models.Model):
    owner = models.ForeignKey(to=User)
    email = models.EmailField()
    text  = models.TextField()
    for_post = models.ForeignKey(to=Post)
