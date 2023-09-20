from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from ReadBookApp.forms import SignUpForm
from . models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import json

# Create your views here.
def homeView(request):
    booksProduct=BookProduct.objects.filter(bestSeller=1)
    return render(request, 'index.html', {'booksProduct': booksProduct})

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
    
# Register or Sign Up
def signupView(request):
    forms=SignUpForm()
    # Action get into method
    if request.method =='POST':
        forms= SignUpForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request,"Successfully Your Account is created.")
            return redirect('signin')
    return render(request, 'ReadBookApp/signup.html',{"forms":forms})

# Login or Sign In 
def signinView(request):
    if request.user.is_authenticated:
       return redirect("/")
    else: 
        if request.method =='POST':
            name = request.POST.get('username')
            password = request.POST.get('password')
            validate = authenticate(request, username=name, password=password)
            if validate is not None:
                login(request,validate)
                messages.success(request,"Successfully Signed In.")
                return redirect('/') # Home Page
            else:
                messages.error(request,"Invalid username or password")
                return redirect('signin')
        return render(request,"ReadBookApp/signin.html")

# logout
def logoutView(request):
  if request.user.is_authenticated:
    logout(request)
    messages.success(request,"Logged out Successfully")
  return redirect("/")
        
# Add to Cart 
def add_to_cart(request):
   if request.headers.get('x-requested-with')=='XMLHttpRequest':
    if request.user.is_authenticated:
      data=json.load(request)
      product_qty=data['product_qty']
      product_id=data['pid']
      product_status = BookProduct.objects.get(id=product_id)
      if product_status:
          if AddCart.objects.filter(user=request.user.id,books_id= product_id):
              return JsonResponse({'status':'Already exist this product.'}, status=200)
          else:
              if product_status.quantity>=product_qty:
                  AddCart.objects.create(user=request.user,books_id= product_id,books_qty = product_qty) 
                  return JsonResponse({'status':'Book Added to Cart Successfully'}, status=200)
              else:
                  return JsonResponse({'status':'Out of Stock'}, status=200)
    else:
      return JsonResponse({'status':'Login to Add Cart'}, status=200)
   else:
    return JsonResponse({'status':'Invalid Access'}, status=200)


def cartView(request):
    if request.user.is_authenticated:
        cart = AddCart.objects.filter(user=request.user)
        return render(request, 'ReadBookApp/cart.html',{'cart': cart})
    else:
        messages.error(request,"Login user only allowed")
        return redirect('/')
