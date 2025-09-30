from django.urls import path
from .views import list_books, LibraryDetailView, list_books
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('books', list_books, name='book_list'),
    path('library', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]