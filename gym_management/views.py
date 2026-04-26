from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import MembershipPlan
from .serializers import MembershipPlanSerializer

class MembershipPlanList(generics.ListCreateAPIView):
    queryset = MembershipPlan.objects.all()
    serializer_class = MembershipPlanSerializer
    permission_classes = [AllowAny]  # Plans sab dekh sakte hain
