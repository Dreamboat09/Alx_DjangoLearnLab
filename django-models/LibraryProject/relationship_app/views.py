from django.shortcuts import render
from .models import Book

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'relationship_app/list_books.html', context)



from django.views.generic.detail import DetailView
from .models import Library

class LibraryView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'