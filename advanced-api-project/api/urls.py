from django.urls import path
from .views import BookCreateView, BookListView, BookDetailView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/create/', BookCreateView.as_view(), name='book_create'),
    path('books/<int:id>/', BookDetailView.as_view(), name='book_detail'),
    path('books/update/<int:id>/', BookUpdateView.as_view(), name='book_update'),
    path('books/delete/<int:id>/', BookDeleteView.as_view(), name='book_delete' ),
]
