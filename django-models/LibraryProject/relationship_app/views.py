from django.shortcuts import render

# Create your views here.
from .models import Book Author Library Librarian


def listbook(request):
    book = Book.object.all
    return render (request, ) 