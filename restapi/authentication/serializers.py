from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(max_length=50, unique=True)
    # email = serializers.EmailField(unique=True, max_length=100)
    # phone_number = serializers.CharField(
    #     unique=True, null=False, max_length=10)
    # password = serializers.CharField(min=10)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password']
        
    def validate(self, attrs):
        username_exists = User.objects.filter(username = attrs['username']).exists()
        email_exists = User.objects.filter(username = attrs['email']).exists()
        phone_number_exists = User.objects.filter(username = attrs['phone_number']).exists()
        
        if username_exists:
            raise serializers.ValidationError(detail = "Username already exists please choose another name")
        
        if email_exists:
            raise serializers.ValidationError(detail = "email already exists please choose another name")
        
        if phone_number_exists:
            raise serializers.ValidationError(detail = "phone number already exists please choose another name")
        
        return super().validate(attrs)
