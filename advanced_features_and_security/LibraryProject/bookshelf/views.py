from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import permission_required

# Create your views here.

@permission_required('bookshelf.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'bookshelf/view_books.html', context)

@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request, books):
    if request.method == 'POST':
        books = Book.objects.create(
            title=request.POST['title'],
            author=request.POST['author'],x
            published_date=request.POST['published_date']
        )
        books.save()
        return render(request, 'bookshelf/view_books.html', {'books': Book.objects.all()})
    return render(request, 'bookshelf/add_book.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.published_date = request.POST['published_date']
        book.save()
        return render(request, 'bookshelf/view_books.html', {'books': Book.objects.all()})
    return render(request, 'bookshelf/edit_book.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return render(request, 'bookshelf/view_books.html', {'books': Book.objects.all()})


