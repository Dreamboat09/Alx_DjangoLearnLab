from django.urls import path
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('admins/', admin_view.admin_view, name='admins'),
    path('librarians/', librarian_view.librarian_view, name='librarians'),
    path('members/', member_view.member_view, name='members'),
]