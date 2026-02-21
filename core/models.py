from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Student(AbstractUser):
    stud_id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    stud_enrollment_date = models.DateField(auto_now_add=True)
    stud_expiry_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.username