from .models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    """Retrieve all books written by a specific author."""
    books = Book.objects.filter(author__name=author_name)
    return books


def get_books_in_library(library_name):
    """Retrieve all books available in a specific library."""
    books = Library.objects.get(name=library_name)
    return books.all()

def get_librarian_of_library(library_name):
    """Retrieve the librarian of a specific library."""
    librarians = Librarian.objects.get(library__name=library_name)
    return librarians