from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def is_admin(user):
    return user.userprofile.role == "Admin"

@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse ('welcome to admin view')