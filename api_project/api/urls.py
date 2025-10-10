from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'), #map to the BookList view
]
