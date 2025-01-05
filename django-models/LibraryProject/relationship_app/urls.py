from django.urls import path
from .views import list_books, LibraryDetailView

urlspatterns = [
    path('book/', list_books, name='book'),
    path('library/', LibraryDetailView.as_views(), name='library')
]