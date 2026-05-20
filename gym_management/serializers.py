from rest_framework import serializers
from .models import MembershipPlan

class MembershipPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipPlan
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Attendance
        fields = ['id', 'user', 'username', 'date', 'check_in_time', 'status']
