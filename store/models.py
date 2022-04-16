import uuid
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# I have created a Profile model. 

class Profile(models.Model):
    User_name = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    First_name = models.CharField(max_length=50, blank=True,null=True)
    Last_name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=254)
    created = models.DateTimeField(auto_now_add=True)
    Id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)

    def __str__(self):
        return str(self.User_name.username)

class Store(models.Model):
    owner = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True, blank=True)
    store_name = models.CharField(max_length=100, blank=True,null=True)
    state = models.CharField(max_length=100, blank=True,null=True)
    Address = models.TextField(null=True,blank=True)
    Books = models.ManyToManyField('Books',blank=True)
    created = models.DateTimeField(auto_now_add=True)
    Id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.store_name

# 2 stores can have same books thats why many to many relationship.

class Books(models.Model):
    Book_name = models.CharField(max_length=100, blank=True,null=True)
    Author_name = models.CharField(max_length=100, blank=True,null=True)
    Book_id  = models.CharField(max_length=30,blank=True,null=True)
    Book_price = models.DecimalField(max_digits=20, decimal_places=2,blank=True,null=True)
    Numb_books = models.IntegerField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    Id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.Book_name