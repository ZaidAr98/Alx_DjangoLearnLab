from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookList

router = DefaultRouter()
router.register(r'books', BookViewSet)
#url
urlpatterns = [
    path('api/', include(router.urls)),
    path('books/', BookList.as_view(), name='list_books'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
