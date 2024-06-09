from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.conf import settings
from .models import *
import jwt

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Specify the model to be serialized
        fields = ['username', 'email', 'password', 'first_name', 'last_name' ,'is_staff' , 'is_superuser']
        extra_kwargs = {'password': {'write_only': True}, 
                        "first_name":{"required":False},
                        "email":{"required":True},
                        "last_name":{"required":False},
                        "is_staff":{"required":False},
                        "is_superuser":{"required":False}
                        }
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
