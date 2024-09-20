from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.



def home(request):
    return render(request,'blog/base.html')  


from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserCreationForm

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect("login")  # Ensure "home" is a valid URL name in your project
        else:
            messages.error(request, "Please correct the error below.")
    
    return render(request, "blog/register.html", {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('profile')  # Redirect to your home page
    else:
        form = AuthenticationForm()  # Create an empty form

    return render(request, 'blog/login.html', {'form': form})


def user_logout(request):
    auth_logout(request) 
    return redirect('login')


from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def profile(request):
    return render(request, 'blog/profile.html', {'user': request.user})


from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
