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

post_like_urls = [
    path('posts/<int:pk>/like/', PostViewSet.as_view({'post': 'like'}), name='post-like'),
    path('posts/<int:pk>/unlike/', PostViewSet.as_view({'post': 'unlike'}), name='post-unlike'),
]

urlpatterns = [
    path('', include(router.urls)),
    path('posts/', include(post_urls)),
    path('feed/', user_feed, name='user-feed'),
    path('', include(post_like_urls)),

]
