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
            'password',
            'role',
            'phone',
            'profile_picture',
            'date_of_birth',
            'address',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # Password nikaal kar baaki data se user banao
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password) # Ye line password ko hash (encrypt) karti hai
        instance.save()
        return instance