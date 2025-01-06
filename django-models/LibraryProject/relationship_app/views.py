from django.shortcuts import render

# Create your views here.
from .models import Book 


def list_books(request):
    Book.objects.all()
    context = {
        'title' : 'book',
        'content': 'this is the list of books',
        }
    return render (request, "relationship_app/list_books.html", context)

 

from django.views.generic.detail import DetailView
from .models import Library, Book


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        lib = self.object
        context ['book'] = Book.objects.filter(Library=lib)
        
        return context
    
    
    
#registrations views
    
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
    
class userlogin(LoginView):
    template_name = "registration/login.html"
           
class userlogout(LogoutView):
    template_name = "registration/logout.html"
    
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        
            return redirect('books')
        
    else:
        form = UserCreationForm
        
    return render(request, 'registration/register.html', {'form' : form } )