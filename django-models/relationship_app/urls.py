from django.urls import path

from .views import list_books, LibraryDetailView,user_login, user_logout, user_register

urlpatterns = [
    path('books/', ClassView, name='list_books'), 
    path('library/<int:pk>/',FunctionView.as_view(), name='LibraryDetailView'), 

     path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', user_register, name='register'),
    

]
