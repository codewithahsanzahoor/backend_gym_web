from django.urls import path
from .views import MembershipPlanList

urlpatterns = [
    path('plans/', MembershipPlanList.as_view(), name='plan-list'),
]
