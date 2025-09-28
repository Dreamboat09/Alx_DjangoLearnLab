from django.shortcuts import render
from .models import Author, Book, Library, Librarian

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'list_books.html', context)



from django.views.generic import DetailView

class LibraryView(DetailView):
    model = Book
    template_name = 'library_detail.html'