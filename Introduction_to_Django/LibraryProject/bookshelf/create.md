from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", published_date="1949-01-01")