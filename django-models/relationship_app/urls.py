from django.urls import path
from .views import ClassView, FunctionView
from .views import "list_books", "LibraryDetailView"
urlpatterns = [
    path('books/', ClassView, name='list_books'), 
    path('library/<int:pk>/',FunctionView.as_view(), name='LibraryDetailView'), 
]
