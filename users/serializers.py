from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=150, min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'id']

    def validate(self, attrs):
        email = attrs.get("email", "")
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {"email": ("Email already exists")})

        return super().validate(attrs)

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
