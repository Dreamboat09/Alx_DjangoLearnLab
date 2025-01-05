from django.urls import path
from .views import LibraryDetailView, list_books

urlspatterns = [
    path('book/', list_books, name='book'),
    path('library/', LibraryDetailView.as_views(), name='library')
]