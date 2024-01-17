from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER = (
        (1, 'HOD'),
        (2, 'INCHARGE'),
        (3, 'STAFF'),
    )

    user_type = models.CharField(choices=USER, max_length=50, default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')


# Department Model
class Department(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Session Model
class Session(models.Model):
    session_start = models.CharField(max_length=100)
    session_end = models.CharField(max_length=100)

    def __str__(self):
        return self.session_start + " To " + self.session_end


# Create Staff Model
class Staff(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    department_id = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    session_id = models.ForeignKey(Session, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name


class Incharge(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.username


# Department Model
class Section(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    incharge = models.ForeignKey(Incharge, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Incharge_Notification Model
class Incharge_Notification(models.Model):
    incharge_id = models.ForeignKey(Incharge, on_delete=models.CASCADE)
    message = models.TextField()
    status = models.IntegerField(null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.incharge_id.admin.first_name + " " + self.incharge_id.admin.last_name


# Staff_Notification Model
class Staff_Notification(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    message = models.TextField()
    status = models.IntegerField(null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.staff_id.admin.first_name + " " + self.staff_id.admin.last_name


class Incharge_Staff_Notification(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    message = models.TextField()
    status = models.IntegerField(null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.staff_id.admin.first_name + " " + self.staff_id.admin.last_name


# Incharge_Leave Model
class Incharge_Leave(models.Model):
    incharge_id = models.ForeignKey(Incharge, on_delete=models.CASCADE)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100, null=True)
    start_time = models.CharField(max_length=100, null=True)
    end_time = models.CharField(max_length=100, null=True)
    message = models.TextField()
    status = models.IntegerField(null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.incharge_id.admin.first_name + " " + self.incharge_id.admin.last_name


# Staff_Leave Model
class Staff_Leave(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100, null=True)
    start_time = models.CharField(max_length=100, null=True)
    end_time = models.CharField(max_length=100, null=True)
    message = models.TextField()
    status = models.IntegerField(null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.staff_id.admin.first_name + " " + self.staff_id.admin.last_name


# Incharge_Feedback Model
class Incharge_Feedback(models.Model):
    incharge_id = models.ForeignKey(Incharge, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    status = models.IntegerField(null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.incharge_id.admin.first_name + " " + self.incharge_id.admin.last_name


# Staff_Feedback Model
class Staff_Feedback(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    status = models.IntegerField(null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.staff_id.admin.first_name + " " + self.staff_id.admin.last_name


# Staff_Feedback_Incharge Model
class Staff_Feedback_Incharge(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    feedback_incharge = models.TextField()
    feedback_incharge_reply = models.TextField()
    status = models.IntegerField(null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.staff_id.admin.first_name + " " + self.staff_id.admin.last_name


# Staff Attendance Model
class Attendance(models.Model):
    section_id = models.ForeignKey(Section, on_delete=models.DO_NOTHING)
    attendance_date = models.DateField()
    session_id = models.ForeignKey(Session, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.section_id.name


# Staff Attendance_Report Model
class Attendance_Report(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.DO_NOTHING)
    attendance_id = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.staff_id.admin.first_name + " " + self.staff_id.admin.last_name


# Incharge_Attendance Model
class Incharge_Attendance(models.Model):
    section_id = models.ForeignKey(Section, on_delete=models.DO_NOTHING)
    incharge_attendance_date = models.DateField()
    session_id = models.ForeignKey(Session, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.section_id.name


# Incharge_Attendance_Report Model
class Incharge_Attendance_Report(models.Model):
    incharge_id = models.ForeignKey(Incharge, on_delete=models.DO_NOTHING)
    incharge_attendance_id = models.ForeignKey(Incharge_Attendance, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.incharge_id.admin.first_name + " " + self.incharge_id.admin.last_name