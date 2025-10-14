from django.urls import path
from .views import BookCreateView, BookListView, BookDetailView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book_list'),
    path('add/', BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('update/<int:pk>/', BookUpdateView.as_view(), name='book_detail'),
    path('delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete' ),
]
