from django.shortcuts import render

from relationship_app.decoraters import custom_user_passes_test
from .models import Book
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
# from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login,logout 
from django.contrib.auth import logout as auth_logout

def list_books(request):
    books = Book.objects.all()  
    return render(request, 'relationship_app/list_books.html', {'books': books})

from django.views.generic.detail import DetailView
from .models import Library


def home(request):
    return render(request, 'relationship_app/home.html')  

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html' 
    context_object_name = 'library'




def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')  # Redirect to your home page
    else:
        form = AuthenticationForm()  # Create an empty form

    return render(request, 'relationship_app/login.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth import login as AuthLogin
from django.contrib.auth.forms import UserCreationForm


def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')  # Redirect to the login page or any desired page
    
    return render(request, 'relationship_app/register.html', {'form': form})

def user_logout(request):
    auth_logout(request)  # Call Django's built-in logout function
    return redirect('login')



from django.contrib.auth.decorators import user_passes_test

# # Check if the user is an Admin
def is_admin(user):
    return user.userprofile.role == 'Admin'

# Check if the user is a Librarian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

# Check if the user is a Member
def is_member(user):
    return user.userprofile.role == 'Member'

# Admin view
@custom_user_passes_test(
    test_func=is_admin,
    redirect_url='home',
    error_message='You do not have the required permissions to access this page.'
)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@custom_user_passes_test(
    test_func=is_librarian,
    redirect_url='home',
    error_message='You do not have the required permissions to access this page.'
)
# Librarian view

def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@custom_user_passes_test(
    test_func=is_member,
    redirect_url='home',
    error_message='You do not have the required permissions to access this page.'
)
# Member view

def member_view(request):
    return render(request, 'relationship_app/member_view.html')



from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden

from .models import Book, Author

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    allowed_users = ['zaid']  # Specify the allowed usernames here
    
    if request.user.username not in allowed_users:
        return HttpResponseForbidden("You don't have permission to access this page.")
    
    if request.method == "POST":
        title = request.POST.get('title')
        author_name = request.POST.get('author')
        published_date = request.POST.get('published_date')

        # Get or create the author instance
        author, created = Author.objects.get_or_create(name=author_name)
        
        # Create the book with the author instance
        Book.objects.create(title=title, author=author, published_date=published_date)
        return redirect('list_books')
    
    return render(request, 'relationship_app/add_book.html')


@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    allowed_users = ['zaid']
    if request.user.username not in allowed_users:
        return HttpResponseForbidden("You don't have permission to access this page.")
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.published_date = request.POST.get('published_date')
        book.save()
        return redirect('list_books')
    return render(request, 'relationship_app/edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    allowed_users = ['zaid']
    if request.user.username not in allowed_users:
        return HttpResponseForbidden("You don't have permission to access this page.")
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})
