from django.urls import path
from .views import (
    ListView, DetailView,CreateView, 
    UpdateView, DeleteView
)
from rest_framework.authtoken.views import obtain_auth_token
# URL patterns for the Book API views
urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('books/', ListView.as_view(), name='book-list'),
    path('books/<int:pk>/', DetailView.as_view(), name='book-detail'),
    path('books/create/', CreateView.as_view(), name='book-create'),
    path('books/update/<int:pk>/', UpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', DeleteView.as_view(), name='book-delete'),
]
