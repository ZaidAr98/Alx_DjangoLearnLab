# posts/views.py
from rest_framework import viewsets, permissions,status, generics
from .models import Post, Comment,Like
from .serializers import PostSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.shortcuts import get_object_or_404
from notifications.models import Notification
from rest_framework.decorators import action
from rest_framework.response import Response

class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True
       
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'content']
    filterset_fields = ['author__username']

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user
         # Use get_or_create to prevent duplicate likes
        like, created = Like.objects.get_or_create(user=user, post=post)

        if not created:
            return Response({'detail': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create notification if the post author is not the user
        if post.author != user:
            Notification.objects.create(
                recipient=post.author,
                actor=user,
                verb='liked your post',
                target=post
            )

        return Response({'detail': 'Post liked.'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def unlike(self, request, pk=None):
         post = generics.get_object_or_404(Post, pk=pk)
         user = request.user
            # 
         try:
            like = Like.objects.get(user=user, post=post)
            like.delete()
            return Response({'detail': 'Post unliked.'}, status=status.HTTP_200_OK)
         except Like.DoesNotExist:
            return Response({'detail': 'You have not liked this post.'}, status=status.HTTP_400_BAD_REQUEST)


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):

    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_queryset(self):
        return Comment.objects.all().filter(post_id=self.kwargs['post_pk']).order_by('-created_at')

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs['post_pk'])
        comment =  serializer.save(author=self.request.user, post=post)
        if post.author != self.request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=self.request.user,
                verb='commented on your post',
                target=post
            )



# posts/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import PostSerializer
from rest_framework import permissions

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def user_feed(request):
    user = request.user
    following_users = user.following.all()
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    serializer = PostSerializer(posts, many=True, context={'request': request})
    return Response(serializer.data)