from django.shortcuts import render, redirect, HttpResponse
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
def genreListView(request,name): 
    if(Genre.objects.filter(name=name,status=0)):
        booksProduct=BookProduct.objects.filter(genre__name=name)
        return render(request, 'ReadBookApp/books.html',{'booksProduct':booksProduct,'genre_name':name})

    else:
        messages.warning(request,"No genre of that kind exists.")
        return redirect('genre')
    
# Book Details
def bookDetailsView(request,genrename,bookname):
    if(Genre.objects.filter(name=genrename,status=0)):
        if(BookProduct.objects.filter(bookName=bookname,bookStatus=0)):
            books = BookProduct.objects.filter(bookName=bookname,bookStatus=0).first()
            return render(request,"ReadBookApp/bookDetails.html",{'books':books})
        else:
            messages.warning(request,"No book of that kind exists.")
            return redirect('genre')
    
    else:
        messages.warning(request,"No genre of that kind exists.")
        return redirect('genre')