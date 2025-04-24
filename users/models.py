from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Farm Manager'),
        ('worker', 'Field Worker'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='worker')

    def _str_(self):
        return self.username