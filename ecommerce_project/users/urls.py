'''This is the urls.py file.

It contains all the paths of users app and the views to call for those paths.
'''

from django.urls import path
from django.contrib import admin
from . import views


app_name = 'users'
urlpatterns = [
    path('home', views.index, name='index'),
    path('updateprofile', views.updateprofile, name='updateprofile'),
    path('shopsignup', views.shopsignup, name='shopsignup'),
    path('approval_requests', views.all_approval_requests,
         name='all_approval_requests'),
    path('approval_requests/<int:user_id>/',
         views.user_approval_requests, name='user_approval_requests'),
    path('admin_approval', views.admin_approval, name='admin_approval'),
    path('shopusers', views.shopusers, name="shopusers"),
]
