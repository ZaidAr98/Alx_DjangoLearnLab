from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import admin_view, librarian_view, member_view
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', ClassView, name='list_books'), 
    path('library/<int:pk>/',FunctionView.as_view(), name='LibraryDetailView'), 
     path('login/', LoginView.as_view(template_name='relationship_app/templates/relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/templates/relationship_app/logout.html'), name='logout'),
    path('register/', views.register.as_view(), name='register'),
       path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),

]


from django.urls import path


urlpatterns = [
 
]
