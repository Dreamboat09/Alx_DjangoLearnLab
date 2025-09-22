from bookshelf.models import Book

books = Book.objects.all()

# getting the result to the standard output

print(book)

<QuerySet [<Book: 1984>]>