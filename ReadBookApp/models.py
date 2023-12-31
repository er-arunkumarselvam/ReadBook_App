from django.db import models
from django.contrib.auth.models import User
import datetime
import os

# Create your models here.
# To handle image name and upload time 
def getFileName(request, filename):
    now_time = datetime.datetime.now().strftime("%Y-%m-%d%H:%M:%S")
    new_filename = "%s%s" % (now_time, filename)
    return os.path.join('uploads/', new_filename) 

# create a genre or category class
class Genre(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    image = models.ImageField(upload_to = getFileName, null=True, blank=True)
    description = models.TextField(max_length=500,  null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0-show,1-Hidden")
    createdAt = models.DateTimeField(auto_now_add=True)
    
    # Overloading __str__ 
    def __str__(self):
        return self.name

def getFileName(request, filename):
    now_time = datetime.datetime.now().strftime("%Y-%m-%d%H:%M:%S")
    new_filename = "%s%s" % (now_time, filename)
    return os.path.join('uploads/books', new_filename) 
# create a books or products class
class BookProduct(models.Model):
    # Create a foreign key in Genre
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    
    bookName = models.CharField(max_length=255, null=False, blank=False)
    authorName = models.CharField(max_length=255, null=False, blank=False)
    publicationName = models.CharField(max_length=255, null=False, blank=False)
    LANGUAGE_CHOICE=[
        ('ta','TAMIL'),
        ('en','ENGLISH'),
        ('fr','FRENCH'),
        ('no','NONE'),  
    ]
    bookLanguage = models.CharField(max_length=2,choices=LANGUAGE_CHOICE, default='en')
    quantity = models.IntegerField(null=False, blank=False)
    buyingPrice = models.FloatField(null=False, blank=False)
    sellingPrice = models.FloatField(null=False, blank=False)
    discountPrice = models.FloatField(null=False, blank=False)
    bookImage = models.ImageField(upload_to = getFileName, null=True, blank=True)
    bookDecription = models.TextField(max_length=1000,  null=False, blank=False)
    bookStatus = models.BooleanField(default=False, help_text="0-show,1-Hidden")
    bestSeller = models.BooleanField(default=False, help_text="0-normal,1-bestseller")
    createAt = models.DateTimeField(auto_now_add=True)
    
    # Overloading __str__ 
    def __str__(self): 
        return self.bookName
    
# Add to Cart
class AddCart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    books=models.ForeignKey(BookProduct, on_delete=models.CASCADE)
    books_qty = models.IntegerField(null=False, blank=False)
    createAt = models.DateTimeField(auto_now_add=True)
    
    @property # decorators
    def total_price(self):
        return self.books_qty*self.books.discountPrice
    