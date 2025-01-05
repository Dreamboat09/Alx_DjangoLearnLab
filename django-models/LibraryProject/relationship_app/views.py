from django.shortcuts import render

# Create your views here.
from .models import Book 


def listbook(request):
    Book.objects.all()
    context = {
        'title' : 'book',
        'content': 'this is the list of books',
        }
    return render (request, "relationship_app/list_books.html", context)

 

from django.views.generic.detail import DetailView
from .models import Library, Book


class listbookinlibrary(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        lib = self.object
        context ['book'] = Book.objects.filter(Library=lib)
        
        return context