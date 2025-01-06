from django.urls import path, include
from .views import list_books, LibraryDetailView, userlogin, userlogout, register

urlpatterns = [
    path('accounts/', include([
        path('login/', userlogin.as_view(), name='login'),
        path('logout/', userlogout.as_view(), name='logout'),
        path('register/', register, name='register'),
        ])),
    path('book/', list_books, name='book'),
    path('library/', LibraryDetailView.as_view(), name='library'),
]