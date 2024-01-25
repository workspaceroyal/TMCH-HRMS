from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


class UserModel(UserAdmin):
    list_display = ['username', 'user_type']


admin.site.register(CustomUser, UserModel)

# Department model Register
admin.site.register(Department)

# Session model Register
admin.site.register(Session)

# Staff Model Register
admin.site.register(Staff)

# Incharge Model Register
admin.site.register(Incharge)

# Section Model Register
admin.site.register(Section)
# Incharge_Notification Model Register
admin.site.register(Incharge_Notification)

# Staff_Notification Model Register
admin.site.register(Staff_Notification)

# Incharge_Staff_Notification Model Register
admin.site.register(Incharge_Staff_Notification)

# Incharge_Leave Model Register
admin.site.register(Incharge_Leave)

# Staff_Leave Model Register
admin.site.register(Staff_Leave)

# Incharge_Feedback Model Register
admin.site.register(Incharge_Feedback)

# Staff_Feedback Model Register
admin.site.register(Staff_Feedback)

# Staff_Feedback_Incharge Model Register
admin.site.register(Staff_Feedback_Incharge)

# Attendance Model Register
admin.site.register(Attendance)

# Attendance_Report Model Register
admin.site.register(Attendance_Report)

# Incharge_Attendance Model Register
admin.site.register(Incharge_Attendance)

# Incharge_Attendance_Report Model Register
admin.site.register(Incharge_Attendance_Report)
