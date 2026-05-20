from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import MembershipPlan, Attendance
from .serializers import MembershipPlanSerializer, AttendanceSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.models import CustomUser
from django.utils import timezone

class AttendanceList(generics.ListCreateAPIView):
    queryset = Attendance.objects.all().order_by('-date', '-check_in_time')
    serializer_class = AttendanceSerializer
    permission_classes = [AllowAny]

class MyAttendanceList(generics.ListAPIView):
    serializer_class = AttendanceSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        if user_id:
            return Attendance.objects.filter(user_id=user_id).order_by('-date')
        return Attendance.objects.none()

class DashboardStats(APIView):
    permission_classes = [AllowAny] # Abhi ke liye AllowAny rakhte hain, baad mein secure karenge

    def get(self, request):
        total_members = CustomUser.objects.filter(role='member').count()
        total_trainers = CustomUser.objects.filter(role='trainer').count()
        active_plans = MembershipPlan.objects.count()
        today_attendance = Attendance.objects.filter(date=timezone.now().date()).count()
        
        # Abhi ke liye revenue mock kar dete hain kyunke payment model nahi hai
        total_revenue = 15400 

        data = {
            "totalMembers": total_members,
            "totalTrainers": total_trainers,
            "activePlans": active_plans,
            "todayAttendance": today_attendance,
            "totalRevenue": total_revenue,
            "memberTrend": "+12%", # Ye baad mein logic se calculate karenge
            "revenueTrend": "+4.2%",
            "attendanceTrend": "-2%"
        }
        return Response(data)

class MembershipPlanList(generics.ListCreateAPIView):
    queryset = MembershipPlan.objects.all()
    serializer_class = MembershipPlanSerializer
    permission_classes = [AllowAny]  # Plans sab dekh sakte hain
