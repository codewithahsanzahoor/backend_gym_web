from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('trainer', 'Trainer'),
        ('member', 'Member'),
    )

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='member'
    )
    phone = models.CharField(max_length=15, blank=True)
    profile_picture = models.ImageField(
        upload_to='profiles/',
        blank=True,
        null=True
    )
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.username} ({self.role})"