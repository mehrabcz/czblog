# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post,Comment,ContactMe,Category

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(ContactMe)
admin.site.register(Category)
