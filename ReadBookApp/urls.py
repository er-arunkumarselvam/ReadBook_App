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
   path("cart",views.cartView,name="cart"),
   path("genre/<str:name>",views.genreListView,name="genre"),
   path("book-details/<str:genrename>/<str:bookname>",views.bookDetailsView,name="book-details"),
   path("signup",views.signupView,name="signup"),
   path("signin",views.signinView,name="signin"),
   path("logout",views.logoutView,name="logout"),
   path('addtocart',views.add_to_cart,name="addtocart"),
] 