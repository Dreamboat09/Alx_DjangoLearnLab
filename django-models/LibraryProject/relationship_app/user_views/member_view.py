from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def is_member(user):
    return user.role == "Member"

@user_passes_test(is_member)
def member_view(request):
    return HttpResponse ('welcome to member view')