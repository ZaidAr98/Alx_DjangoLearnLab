from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics, permissions
from .models import Notification
from .serializers import NotificationSerializer

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-timestamp')


@api_view(['POST'])
def mark_as_read(request, pk):
    try:
        notification = Notification.objects.get(pk=pk, recipient=request.user)
    except Notification.DoesNotExist:
        return Response({'detail': 'Notification not found.'}, status=status.HTTP_404_NOT_FOUND)
    notification.unread = False
    notification.save()
    return Response({'detail': 'Notification marked as read.'}, status=status.HTTP_200_OK)