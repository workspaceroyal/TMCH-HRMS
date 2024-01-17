# from django.shortcuts import render, redirectfrom django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import Department, Session, CustomUser, Staff, Incharge, Section, Incharge_Notification, Incharge_Leave, \
    Incharge_Feedback, Attendance, Attendance_Report, Staff_Notification, Staff_Feedback_Incharge, \
    Incharge_Staff_Notification, Incharge_Attendance_Report
from django.contrib import messages


@login_required(login_url='/')
def HOME(request):
    return render(request, 'Incharge/home.html')


@login_required(login_url='/')
def NOTIFICATIONS(request):
    incharge = Incharge.objects.filter(admin=request.user.id)

    for i in incharge:
        incharge_id = i.id

    notification = Incharge_Notification.objects.filter(incharge_id=incharge_id)

    context = {
        'notification': notification
    }

    return render(request, 'Incharge/incharge_notification.html', context)


@login_required(login_url='/')
def NOTIFICATION_MARKING(request, status):
    notification = Incharge_Notification.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect('incharge_notifications')


@login_required(login_url='/')
def SEND_STAFF_NOTIFICATION(request):
    staff = Staff.objects.all()
    incharge_see_notification = Incharge_Staff_Notification.objects.all().order_by('-id')[0:5]

    context = {
        'staff': staff,
        'incharge_see_notification': incharge_see_notification,
    }
    return render(request, 'Incharge/staff_notification.html', context)


@login_required(login_url='/')
def SAVE_STAFF_NOTIFICATION(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        message = request.POST.get('message')

        staff = Staff.objects.get(admin = staff_id)
        incharge_notification = Incharge_Staff_Notification(
            staff_id = staff,
            message = message,
        )
        incharge_notification.save()
        messages.success(request, 'Notification are Successfully Sent')
        return redirect('incharge_send_staff_notification')



@login_required(login_url='/')
def APPLY_INCHARGE_LEAVE_FULL_DAY(request):
    incharge = Incharge.objects.filter(admin=request.user.id)

    for i in incharge:
        incharge_id = i.id

    incharge_leave_history = Incharge_Leave.objects.filter(incharge_id=incharge_id)

    context = {
        'incharge_leave_history': incharge_leave_history,
    }

    return render(request, 'Incharge/apply_leave_full_day.html', context)


@login_required(login_url='/')
def APPLY_INCHARGE_LEAVE_SHORT_TIME(request):
    incharge = Incharge.objects.filter(admin=request.user.id)

    for i in incharge:
        incharge_id = i.id

    incharge_leave_history = Incharge_Leave.objects.filter(incharge_id=incharge_id)

    context = {
        'incharge_leave_history': incharge_leave_history,
    }

    return render(request, 'Incharge/apply_leave_short_time.html', context)


@login_required(login_url='/')
def SAVE_APPLY_INCHARGE_LEAVE(request):
    if request.method == "POST":
        leave_start_date = request.POST.get('leave_start_date')
        leave_end_date = request.POST.get('leave_end_date')

        leave_start_time = request.POST.get('leave_start_time')
        leave_end_time = request.POST.get('leave_end_time')

        leave_message = request.POST.get('leave_message')

        incharge = Incharge.objects.get(admin=request.user.id)

        leave = Incharge_Leave(
            incharge_id=incharge,
            start_date=leave_start_date,
            end_date=leave_end_date,

            start_time=leave_start_time,
            end_time=leave_end_time,

            message=leave_message,
        )
        leave.save()

        messages.success(request, 'Leave Application are Successfully Saved')
        return redirect('apply_incharge_leave_full_day')


@login_required(login_url='/')
def INCHARGE_FEEDBACK(request):
    incharge_id = Incharge.objects.get(admin=request.user.id)

    feedback_history = Incharge_Feedback.objects.filter(incharge_id=incharge_id)

    context = {
        'feedback_history': feedback_history,
    }

    return render(request, 'Incharge/incharge_feedback.html', context)


@login_required(login_url='/')
def INCHARGE_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback = request.POST.get('feedback')

        incharge = Incharge.objects.get(admin=request.user.id)

        feedback = Incharge_Feedback(
            incharge_id=incharge,
            feedback=feedback,
            feedback_reply="",
        )
        feedback.save()

        messages.success(request, 'Incharge Feedback are Successfully Saved')
        return redirect('incharge_feedback')


@login_required(login_url='/')
def INCHARGE_STAFF_FEEDBACK(request):
    feedback_incharge = Staff_Feedback_Incharge.objects.all()
    feedback_incharge_history = Staff_Feedback_Incharge.objects.all().order_by('-id')[0:5]

    context = {
        'feedback_incharge': feedback_incharge,
        'hod_feedback_incharge_history': feedback_incharge_history,
    }

    return render(request, 'Incharge/staff_feedback.html', context)


@login_required(login_url='/')
def INCHARGE_STAFF_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback_incharge_id = request.POST.get('feedback_incharge_id')
        feedback_incharge_reply = request.POST.get('feedback_incharge_reply')

        feedback_incharge = Staff_Feedback_Incharge.objects.get(id = feedback_incharge_id)
        feedback_incharge.feedback_incharge_reply = feedback_incharge_reply

        feedback_incharge.status = 1
        feedback_incharge.save()

        return redirect('incharge_staff_feedback')


def INCHARGE_STAFF_TAKE_ATTENDANCE(request):
    incharge_id = Incharge.objects.get(admin=request.user.id)

    section = Section.objects.filter(incharge=incharge_id)
    session = Session.objects.all()
    action = request.GET.get('action')

    staffs = None
    get_section = None
    get_session = None

    if action is not None:
        if request.method == "POST":
            section_id = request.POST.get('section_id')
            session_id = request.POST.get('session_id')

            get_section = Section.objects.get(id=section_id)
            get_session = Session.objects.get(id=session_id)

            section = Section.objects.filter(id=section_id)
            for i in section:
                staff_id = i.department.id
                staffs = Staff.objects.filter(department_id=staff_id)

    context = {
        'action': action,
        'section': section,
        'session': session,
        'get_section': get_section,
        'get_session': get_session,
        'staffs': staffs,
    }

    return render(request, 'Incharge/staff_take_attendance.html', context)


def INCHARGE_STAFF_SAVE_ATTENDANCE(request):
    if request.method == "POST":
        section_id = request.POST.get('section_id')
        session_id = request.POST.get('session_id')
        attendance_date = request.POST.get('attendance_date')
        staff_id = request.POST.getlist('staff_id')

        get_section = Section.objects.get(id=section_id)
        get_session = Session.objects.get(id=session_id)

        attendance = Attendance(
            section_id=get_section,
            attendance_date=attendance_date,
            session_id=get_session,
        )
        attendance.save()

        for i in staff_id:
            stud_id = i
            int_stud = int(stud_id)

            p_staffs = Staff.objects.get(id=int_stud)

            attendance_report = Attendance_Report(
                staff_id=p_staffs,
                attendance_id=attendance,
            )
            attendance_report.save()

    return redirect('incharge_staff_take_attendance')


def INCHARGE_STAFF_VIEW_ATTENDANCE(request):
    incharge_id = Incharge.objects.get(admin=request.user.id)

    section = Section.objects.filter(incharge_id=incharge_id)
    session = Session.objects.all()

    action = request.GET.get('action')

    get_section = None
    get_session = None
    attendance_date = None
    attendance_report = None

    if action is not None:
        if request.method == "POST":
            section_id = request.POST.get('section_id')
            session_id = request.POST.get('session_id')
            attendance_date = request.POST.get('attendance_date')

            get_section = Section.objects.get(id=section_id)
            get_session = Session.objects.get(id=session_id)
            attendance = Attendance.objects.filter(section_id=get_section, attendance_date=attendance_date, )
            for i in attendance:
                attendance_id = i.id
                attendance_report = Attendance_Report.objects.filter(attendance_id=attendance_id)

    context = {
        'section': section,
        'session': session,
        'action': action,
        'get_section': get_section,
        'get_session': get_session,
        'attendance_date': attendance_date,
        'attendance_report': attendance_report,
    }

    return render(request, 'Incharge/staff_view_attendance.html', context)


@login_required(login_url='/')
def INCHARGE_VIEW_ATTENDANCE(request):
    incharge = Incharge.objects.get(admin = request.user.id)
    sections = Section.objects.all()

    action = request.GET.get('action')

    get_section = None
    incharge_attendance_report = None

    if action is not None:
        if request.method == "POST":
            section_id = request.POST.get('section_id')
            get_section = Section.objects.get(id=section_id)

            incharge_attendance_report = Incharge_Attendance_Report.objects.filter(incharge_id=incharge, incharge_attendance_id__section_id=section_id)

    context = {
        'sections': sections,
        'action': action,
        'get_section': get_section,
        'incharge_attendance_report': incharge_attendance_report,
    }

    return render(request, 'Incharge/incharge_view_attendance.html', context)
