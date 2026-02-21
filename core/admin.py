from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Student

# This ensures the admin treats your Student like a User (password hashing, etc.)
admin.site.register(Student, UserAdmin)