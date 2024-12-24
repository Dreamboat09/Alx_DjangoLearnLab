from django.shortcuts import render

# Create your views here.
from .models import Book


def listbook(request):
    Book.object.all()
    context = {
        'title' : 'book',
        'content': 'this is the list of books'
        }
    return render (request, "relationship_app/list_books.html", Book.object.all())

 

from django.views.generic import ListView

class listbookinlibrary(ListView):
    model = Book
    template_name = "books/library_detail.html"
    context_object_name = "books"