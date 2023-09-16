from django.shortcuts import render, redirect
from . models import *
from django.contrib import messages

# Create your views here.
def homeView(request):
    return render(request, 'index.html')

# Genre Option
def genreView(request):
    genre=Genre.objects.filter(status=0)
    return render(request, 'ReadBookApp/genre.html',{'genre':genre})
# Genre List 
def genreList(request,name): 
    if(Genre.objects.filter(name=name,status=0)):
        booksProduct=BookProduct.objects.filter(genre__name=name)
        return render(request, 'ReadBookApp/books.html',{'booksProduct':booksProduct})

    else:
        messages.warning(request,"No genre of that kind exists.")
        return redirect('genre')
    
    