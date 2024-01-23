# from django.shortcuts import render, redirectfrom django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import Department, Session, CustomUser, Staff, Incharge, Section, Incharge_Notification, Incharge_Leave, \
    Incharge_Feedback, Attendance, Attendance_Report, Staff_Notification, Staff_Feedback, Staff_Leave, \
    Staff_Feedback_Incharge, Incharge_Staff_Notification
from django.contrib import messages


@login_required(login_url='/')
def HOME(request):
    return render(request, 'Staff/home.html')


@login_required(login_url='/')
def NOTIFICATIONS(request):
    global staff_id
    staff = Staff.objects.filter(admin=request.user.id)

    for i in staff:
        staff_id = i.id

    notification = Staff_Notification.objects.filter(staff_id=staff_id)

    context = {
        'notification': notification
    }

    return render(request, 'Staff/staff_notification.html', context)


@login_required(login_url='/')
def NOTIFICATION_MARKING(request, status):
    notification = Staff_Notification.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect('staff_notifications')


@login_required(login_url='/')
def INCHARGE_NOTIFICATIONS(request):
    global staff_id
    staff = Staff.objects.filter(admin=request.user.id)

    for i in staff:
        staff_id = i.id

    incharge_notification = Incharge_Staff_Notification.objects.filter(staff_id=staff_id)

    context = {
        'incharge_notification': incharge_notification
    }

    return render(request, 'Staff/incharge_staff_notification.html', context)


@login_required(login_url='/')
def INCHARGE_NOTIFICATION_MARKING(request, status):
    incharge_notification = Incharge_Staff_Notification.objects.get(id=status)
    incharge_notification.status = 1
    incharge_notification.save()
    return redirect('incharge_staff_notifications')


@login_required(login_url='/')
def APPLY_STAFF_LEAVE_FULL_DAY(request):
    staff = Staff.objects.filter(admin=request.user.id)

    for i in staff:
        staff_id = i.id

    staff_leave_history = Staff_Leave.objects.filter(staff_id=staff_id)

    context = {
        'staff_leave_history': staff_leave_history,
    }

    return render(request, 'Staff/apply_leave_full_day.html', context)


@login_required(login_url='/')
def APPLY_STAFF_LEAVE_SHORT_TIME(request):
    staff = Staff.objects.filter(admin=request.user.id)

    for i in staff:
        staff_id = i.id

    staff_leave_history = Staff_Leave.objects.filter(staff_id=staff_id)

    context = {
        'staff_leave_history': staff_leave_history,
    }

    return render(request, 'Staff/apply_leave_short_time.html', context)


@login_required(login_url='/')
def SAVE_APPLY_STAFF_LEAVE(request):
    if request.method == "POST":
        leave_start_date = request.POST.get('leave_start_date')
        leave_end_date = request.POST.get('leave_end_date')

        leave_start_time = request.POST.get('leave_start_time')
        leave_end_time = request.POST.get('leave_end_time')

        leave_type = request.POST.get('leave_type')
        leave_place = request.POST.get('leave_place')
        staff_designation = request.POST.get('staff_designation')
        signature = request.POST.get('signature')

        leave_reason = request.POST.get('leave_reason')

        staff = Staff.objects.get(admin=request.user.id)

        leave = Staff_Leave(
            staff_id=staff,
            start_date=leave_start_date,
            end_date=leave_end_date,

            start_time=leave_start_time,
            end_time=leave_end_time,

            leave_type=leave_type,
            leave_place=leave_place,
            designation=staff_designation,
            staff_signature=signature,

            leave_reason=leave_reason,
        )
        leave.save()

        messages.success(request, 'Leave Application are Successfully Saved')
        return redirect('apply_staff_leave_full_day')


@login_required(login_url='/')
def STAFF_FEEDBACK(request):
    staff_id = Staff.objects.get(admin=request.user.id)

    feedback_history = Staff_Feedback.objects.filter(staff_id=staff_id)

    context = {
        'feedback_history': feedback_history,
    }

    return render(request, 'Staff/staff_feedback.html', context)


@login_required(login_url='/')
def STAFF_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback = request.POST.get('feedback')

        staff = Staff.objects.get(admin=request.user.id)

        feedback = Staff_Feedback(
            staff_id=staff,
            feedback=feedback,
            feedback_reply="",
        )
        feedback.save()

        messages.success(request, 'Staff Feedback are Successfully Saved')
        return redirect('staff_feedback')


@login_required(login_url='/')
def STAFF_FEEDBACK_INCHARGE(request):
    staff_id = Staff.objects.get(admin=request.user.id)

    feedback_incharge_history = Staff_Feedback_Incharge.objects.filter(staff_id=staff_id)

    context = {
        'feedback_incharge_history': feedback_incharge_history,
    }

    return render(request, 'Staff/staff_feedback_incharge.html', context)


@login_required(login_url='/')
def STAFF_FEEDBACK_INCHARGE_SAVE(request):
    if request.method == "POST":
        feedback_incharge = request.POST.get('feedback_incharge')

        staff = Staff.objects.get(admin=request.user.id)

        feedback_incharge = Staff_Feedback_Incharge(
            staff_id=staff,
            feedback_incharge=feedback_incharge,
            feedback_incharge_reply="",
        )
        feedback_incharge.save()

        messages.success(request, 'Staff Feedback are Successfully Saved')
        return redirect('staff_feedback_incharge')


@login_required(login_url='/')
def STAFF_VIEW_ATTENDANCE(request):
    staff = Staff.objects.get(admin = request.user.id)
    sections = Section.objects.filter(department=staff.department_id)

    action = request.GET.get('action')

    get_section = None
    attendance_report = None

    if action is not None:
        if request.method == "POST":
            section_id = request.POST.get('section_id')
            get_section = Section.objects.get(id=section_id)

            attendance_report = Attendance_Report.objects.filter(staff_id=staff, attendance_id__section_id=section_id)

    context = {
        'sections': sections,
        'action': action,
        'get_section': get_section,
        'attendance_report': attendance_report,
    }

    return render(request, 'Staff/staff_view_attendance.html', context)