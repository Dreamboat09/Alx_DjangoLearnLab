from .models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    """Retrieve all books written by a specific author."""
    return Book.objects.filter(author__name=Author.name)

def get_books_in_library(library_name):
    """Retrieve all books available in a specific library."""
    return Book.objects.filter(library_name=Library.name)

def get_librarian_of_library(library_name):
    """Retrieve the librarian of a specific library."""
    return Librarian.objects.get(library__name=Library.name)