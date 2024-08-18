from django.shortcuts import render
from .models import Book
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LogoutView


def list_books(request):
    books = Book.objects.all()  
    return render(request, 'relationship_app/temlates/relationship_app/list_books.html', {'books': books})

from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/temlates/relationship_app/library_detail.html' 
    context_object_name = 'library'



# Registration view using Django's built-in form
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/temlates/relationship_app/register.html'
    success_url = reverse_lazy('login')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to a home page or any other page
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/temlates/relationship_app/login.html', {'form': form})

class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/temlates/relationship_app/logout.html'
