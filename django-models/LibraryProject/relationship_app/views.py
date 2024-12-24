from django.shortcuts import render

# Create your views here.
from .models import Book, Library


def listbook(request):
    Book.objects.all()
    context = {
        'title' : 'book',
        'content': 'this is the list of books'
        }
    return render (request, "relationship_app/list_books.html", context)

 

from django.views.generic import ListView

class listbookinlibrary(ListView):
    model = Book
    Book.objects.get(Library=ListView)
    template_name = "relationship_app/library_detail.html"
    context_object_name = "books"