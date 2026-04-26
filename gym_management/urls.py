from django.urls import path
from .views import MembershipPlanList, DashboardStats

urlpatterns = [
    path('plans/', MembershipPlanList.as_view(), name='plan-list'),
    path('dashboard-stats/', DashboardStats.as_view(), name='dashboard-stats'),
]
