from django.urls import path

from .views import list_books, LibraryDetailView,loginView, logoutView, RegisterView

urlpatterns = [
    path('books/', ClassView, name='list_books'), 
    path('library/<int:pk>/',FunctionView.as_view(), name='LibraryDetailView'), 
       path('login/', loginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),

]
