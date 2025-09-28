from django.urls import path
from .views import book_list, LibraryView

urlpatterns = [
    path('', book_list, name='book_list'),
    path('library', LibraryView.as_view(), name='library_detail'),
]