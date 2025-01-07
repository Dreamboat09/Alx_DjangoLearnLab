from django.contrib import admin

# Register your models here.
from .models import Book, Library, Librarian, Author, UserProfile

admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
admin.site.register(Author)
admin.site.register(UserProfile)