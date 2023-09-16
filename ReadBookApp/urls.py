"""
# ReadBook App
# File: urls.py
# Author: Arunkumar
# Description: To manage the URLs in your application
"""
from django.urls import path
from . import views

urlpatterns=[
   path("",views.homeView,name="home"),
   path("genre",views.genreView,name="genre"),
   path("genre/<str:name>",views.genreList,name="genre"),
] 