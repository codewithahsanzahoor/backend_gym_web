from django.db import models

class MembershipPlan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    period = models.CharField(max_length=50, default='month')  # e.g., month, year
    features = models.JSONField(default=list)  # Hum features ko list ki surat mein save karenge
    is_popular = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    check_in_time = models.TimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Present')

    def __str__(self):
        return f"{self.user.username} - {self.date}"
