from django.urls import path
from . import views

urlpatterns = [
    path('documents/', views.document_list, name='document_list'),
    path('documents/create/', views.create_document, name='create_document'),
    path('documents/<int:pk>/edit/', views.edit_document, name='edit_document'),
    path('documents/<int:pk>/delete/', views.delete_document, name='delete_document'),
]
