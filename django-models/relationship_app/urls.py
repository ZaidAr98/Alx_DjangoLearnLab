from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', ClassView, name='list_books'), 
    path('library/<int:pk>/',FunctionView.as_view(), name='LibraryDetailView'), 
     path('login/', LoginView.as_view(template_name='relationship_app/templates/relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/templates/relationship_app/logout.html'), name='logout'),
    path('register/', views.register.as_view(), name='register'),

]
