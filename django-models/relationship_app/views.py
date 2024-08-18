from django.shortcuts import render
from .models import Book
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect



from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



def list_books(request):
    books = Book.objects.all()  
    return render(request, 'relationship_app/temlates/relationship_app/list_books.html', {'books': books})

from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/temlates/relationship_app/library_detail.html' 
    context_object_name = 'library'




class loginView(LoginView):
    template_name = 'relationship_app/temlates/relationship_app/login.html'

class logoutView(LogoutView):
    template_name = 'relationship_app/temlates/relationship_app/logout.html'

class register(CreateView):
     model = User
    template_name = 'relationship_app/temlates/relationship_app/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
