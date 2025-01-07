from django.urls import path, include
from .views import list_books, LibraryDetailView
from . import views
from .user_views import admin_view, librarian_view, member_view
urlpatterns = [
    path('accounts/', include([
        path('login/', views.LoginView.as_view(template_name='registration/login.html'), name='login'),
        path('logout/', views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
        path('register/', views.register, name='register'),
        ])),
    path('book/', list_books, name='book'),
    path('library/', LibraryDetailView.as_view(), name='library'),
    path('admins/', admin_view.admin_view, name='admins'),
    path('librarians/', librarian_view.librarian_view, name='librarians'),
    path('members/', member_view.member_view, name='members'),
]