from django.urls import path

from .views import list_books, LibraryDetailView,login_view, RegisterView, CustomLogoutView

urlpatterns = [
    path('books/', ClassView, name='list_books'), 
    path('library/<int:pk>/',FunctionView.as_view(), name='LibraryDetailView'), 
     path('login/', LoginView.as_view(), name='login_view'),
    path('logout/', CustomLogoutView.as_view(), name='CustomLogoutView'),
    path('register/', RegisterView.as_view(), name='RegisterView'),
]
