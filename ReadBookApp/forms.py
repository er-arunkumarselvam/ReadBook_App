"""
# Read Book App
# File: forms.py
# Author: Arunkumar
# Description: This file manages user input validation for secure authentication during sign-up and sign-in in Django.
"""
from django.contrib.auth.forms import UserCreationForm
from ReadBookApp.models import User
from django import forms

# Create a Sign Up Form using  User  Creation Form 
class SignUpForm(UserCreationForm):
    # Bootstrap Class Handled
    username = forms.CharField(widget= forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your username'}))
    email = forms.CharField(widget= forms.EmailInput(attrs={'class':'form-control', 'placeholder':'admin@email.com'}))
    password1 = forms.CharField(widget= forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(widget= forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))

    class Meta:
        model=User
        fields = ['username', 'email', 'password1', 'password2' ]
        
    
