from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^about/$',views.about,name='about'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^categories/$',views.categories_list,name='cats'),
    url(r'^post/(?P<id>[0-9]{1,3})$',views.post,name='post'),
    url(r'^category/(?P<id>[0-9]{1,3})$',views.categorypost,name='catposts'),


]

