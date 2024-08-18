from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import admin_view, librarian_view, member_view
from .views import list_books, LibraryDetailView
from . import views

urlpatterns = [
    path('books/', ClassView, name='list_books'), 
    path('library/<int:pk>/',FunctionView.as_view(), name='LibraryDetailView'), 
     path('login/', LoginView.as_view(template_name='relationship_app/templates/relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/templates/relationship_app/logout.html'), name='logout'),
    path('register/', views.register.as_view(), name='register'),
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
    path('books/add/', views.add_book, name='add_book'),

    
    path('books/edit/<int:pk>/', views.edit_book, name='edit_book'),

   
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),

  
    path('books/', views.list_books, name='list_books'),

]







