from django.urls import path

from .views import list_books, LibraryDetailView,loginView, logoutView, register

urlpatterns = [
    path('books/', ClassView, name='list_books'), 
    path('library/<int:pk>/',FunctionView.as_view(), name='LibraryDetailView'), 
     path('login/', loginView.as_view(), name='login'),
    path('logout/', logoutView.as_view(), name='logout'),
    path('register/', register, name='register'),

]
