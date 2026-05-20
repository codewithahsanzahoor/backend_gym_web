from django.urls import path
from .views import MembershipPlanList, DashboardStats, AttendanceList, MyAttendanceList

urlpatterns = [
    path('plans/', MembershipPlanList.as_view(), name='plan-list'),
    path('dashboard-stats/', DashboardStats.as_view(), name='dashboard-stats'),
    path('attendance/', AttendanceList.as_view(), name='attendance-list'),
    path('my-attendance/', MyAttendanceList.as_view(), name='my-attendance'),
]
