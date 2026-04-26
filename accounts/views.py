from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import CustomUser
from .serializers import UserSerializer

class MemberList(generics.ListCreateAPIView):
    # Sirf un users ko filter karo jin ka role 'member' hai
    queryset = CustomUser.objects.filter(role='member').order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [AllowAny] # Baad mein isay IsAdminUser karenge
