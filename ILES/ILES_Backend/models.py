from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'STUDENT'),
        ('work_place_supervisor', 'WORK_PLACE_SUPERVISOR'),
        ('academic_supervisor', 'ACADEMIC_SUPERVISOR'),
        ('intern_admin', 'INTERN_ADMIN'),
    )

    role = models.CharField(max_length=30, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return self.username