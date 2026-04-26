from rest_framework import serializers
from .models import CustomUser


# Serializer kya karta hai:
# MySQL se data aata hai Python object ki form mein
# Serializer us object ko JSON mein convert karta hai
# Bilkul Node mein res.json() jaisa

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username',
            'email',
            'role',
            'phone',
            'profile_picture',
            'date_of_birth',
            'address',
        ]
        # Password kabhi response mein nahi aayega
        extra_kwargs = {
            'password': {'write_only': True}
        }