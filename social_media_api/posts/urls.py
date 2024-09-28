# posts/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet,user_feed

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

post_urls = [
    path('<int:post_pk>/comments/', CommentViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='comment-list'),
    path('<int:post_pk>/comments/<int:pk>/', CommentViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='comment-detail'),
]
urlpatterns = [
    path('', include(router.urls)),
    path('posts/', include(post_urls)),
    path('feed/', user_feed, name='user-feed'),
]
