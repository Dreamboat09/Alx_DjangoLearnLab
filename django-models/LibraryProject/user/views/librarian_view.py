from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def is_librarian(user):
    return user.role == "Librarian"

@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse ('welcome to librarian view')