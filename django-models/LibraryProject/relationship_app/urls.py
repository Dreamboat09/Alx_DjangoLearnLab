from django.urls import path
import views

urlspatterns = [
    path('book/', views.listbook, name='book'),
    path('library/', views.as_views(), name='library')
]