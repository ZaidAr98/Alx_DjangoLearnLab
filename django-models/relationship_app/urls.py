from django.urls import path

# from .views import admin_view, librarian_view, member_view
from .views import list_books, LibraryDetailView,register,user_login,logout
from . import views
from .views import user_logout

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', list_books, name='list_books'), 
    path('library/<int:pk>/',LibraryDetailView.as_view(), name='LibraryDetailView'), 
    path('login/',user_login, name='login'),
  path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    # path('admin-view/', admin_view, name='admin_view'),
    # path('librarian-view/', librarian_view, name='librarian_view'),
    # path('member-view/', member_view, name='member_view'),
    # path('books/add_book/', views.add_book, name='add_book'),
    # path('books/edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    # path('books/delete_book/<int:pk>/', views.delete_book, name='delete_book'),


]







