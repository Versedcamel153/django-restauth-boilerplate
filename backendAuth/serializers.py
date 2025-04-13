from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers

class CustomRegisterSerializer(RegisterSerializer):
    def validate_email(self, email):
        UserModel = get_user_model()
        if UserModel.objects.filter(email=email).exists():
            raise serializers.ValidationError("A user is already registered with this email address.")
        return email
    
