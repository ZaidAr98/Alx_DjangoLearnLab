from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token


User = get_user_model()
register =get_user_model().objects.create_user

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'bio', 'profile_picture']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = register(
            username=validated_data['username'],
            email=validated_data['email'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None),
        )
   

        # Create a token for the new user
        Token.objects.create(user=user)

        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)