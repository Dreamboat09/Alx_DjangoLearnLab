from django.shortcuts import render

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# Create your views here.

class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'book_id'

class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)
        return Book.objects.all()

class BookUpdateView(UpdateAPIView):
    serializer_class = BookSerializer
    permission_classes =  [IsAuthenticatedOrReadOnly]
    lookup_field = 'id'
    lookup_url_kwarg = 'book_id'

    def get_queryset(self):
      if self.request.user is not None:
          return Book.objects.filter(added_by=self.request.user)
      return Book.objects.none()

class BookDeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    lookup_url_kwarg = 'book_id'
