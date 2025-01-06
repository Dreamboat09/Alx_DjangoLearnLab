from django.urls import path, include
from .views import list_books, LibraryDetailView, userlogin, userlogout, register
from . import views
urlpatterns = [
    path('accounts/', include([
        path('login/', userlogin.as_view(template_name='registration/login.html'), name='login'),
        path('logout/', userlogout.as_view(template_name='registration/logout.html'), name='logout'),
        path('register/', views.register, name='register'),
        ])),
    path('book/', list_books, name='book'),
    path('library/', LibraryDetailView.as_view(), name='library'),
]