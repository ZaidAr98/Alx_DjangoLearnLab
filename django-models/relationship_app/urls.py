from django.urls import path
from .views import ClassView, FunctionView

urlpatterns = [
    path('books/', ClassView, name='list_books'), 
    path('library/<int:pk>/',FunctionView.as_view(), name='library_detail'), 
]
