from django.urls import path

from .views import list_books, LibraryDetailView,CustomLoginView, CustomLogoutView, RegisterView

urlpatterns = [
 path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView(), name='register'),

]
