from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


class UserModel(UserAdmin):
    list_display = ['username', 'user_type']


admin.site.register(CustomUser, UserModel)

# Course model Register
admin.site.register(Course)

# Session_Year model Register
admin.site.register(Session_Year)

# Student Model Register
admin.site.register(Student)

# Staff Model Register
admin.site.register(Staff)

# Subject Model Register
admin.site.register(Subject)

# Staff_Notification Model Register
admin.site.register(Staff_Notification)

# Staff_Leave Model Register
admin.site.register(Staff_Leave)

# Staff_Feedback Model Register
admin.site.register(Staff_Feedback)

# Attendance Model Register
admin.site.register(Attendance)

# Attendance_Report Model Register
admin.site.register(Attendance_Report)
