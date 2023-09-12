from django.contrib import admin
from ReadBookApp.models import *

# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    
class BookProductAdmin(admin.ModelAdmin):
    list_display = ('genre','bookName')
    
    
admin.site.register(Genre, GenreAdmin)
admin.site.register(BookProduct, BookProductAdmin)
