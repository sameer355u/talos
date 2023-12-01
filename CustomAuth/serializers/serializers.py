from rest_framework import serializers
from rest_framework.permissions import BasePermission
from CustomAuth.models import User


class APIPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        else:
            return False


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
