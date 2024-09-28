# accounts/views.py
from rest_framework import generics, permissions, status
from .serializers import RegisterSerializer, LoginSerializer, UserProfileSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import CustomUser
from django.contrib.auth import login

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = self.get_queryset().get(id=response.data['id'])
        token, created = Token.objects.get_or_create(user=user)
        response.data['token'] = token.key
        return response

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, created = Token.objects.get_or_create(user=user)
            login(request, user)
            return Response({
                'token': token.key,
                'user_id': user.id,
                'username': user.username
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
