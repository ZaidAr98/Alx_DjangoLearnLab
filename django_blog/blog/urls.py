from django.urls import path
from .views import home,register,user_login,user_logout,profile
from .views import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from . import views

urlpatterns = [
 
    path("register/",register,name='register'),
    path('login/',user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path("profile/",profile,name="profile"),
    path('', ListView.as_view(), name='post-list'),
    path('post/new/', CreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', DetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', UpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', DeleteView.as_view(), name='post-delete'),
]