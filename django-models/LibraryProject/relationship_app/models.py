from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Library(models.Model):
    name = models.CharField(max_length=20)
    books = models.ManyToManyField(Book)
    
    def __str__(self):
        return self.name
    
    
class Librarian(models.Model):
    name = models.CharField(max_length=20)
    library = models.OneToOneField(Library,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
from django.contrib.auth.models import User
    
class UserProfile(models.Model):
    Roles = [
        ('Admin', 'admin'),
        ('Librarian', 'librarian'),
        ('Member', 'member'),
        ]
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    role = models.CharField(max_length=9, choices=Roles, default="Member")
    
    def __str__(self):
        return f'{self.user.username} - {self.role}'