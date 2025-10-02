from django.contrib import admin
from .models import Book, CustomUser

# Register your models here.
#class BookAdmin(admin.ModelAdmin):
#    list_display = ('title', 'author', 'published_date')
#    search_fields = ('title', 'author')
#    list_filter = ('published_date',)

#admin.site.register(Book, BookAdmin)


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'password', 'date_of_birth', 'profile_photo')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('date_joined', 'last_login')

admin.site.register(CustomUser, CustomUserAdmin)