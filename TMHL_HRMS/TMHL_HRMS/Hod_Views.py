from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import Department, Session, CustomUser, Staff, Incharge, Section, Incharge_Notification, Incharge_Leave, \
    Incharge_Feedback, Attendance, Attendance_Report, Staff_Notification, Staff_Feedback, Staff_Leave, \
    Incharge_Attendance, Incharge_Attendance_Report

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


@login_required(login_url='/')
def HOME(request):

    staff_count = Staff.objects.all().count()
    incharge_count = Incharge.objects.all().count()
    department_count = Department.objects.all().count()
    section_count = Section.objects.all().count()

    context = {
        'staff_count': staff_count,
        'incharge_count': incharge_count,
        'department_count': department_count,
        'section_count': section_count,
    }

    return render(request, 'Hod/home.html', context)


# Staff All Function
@login_required(login_url='/')
def ADD_STAFF(request):
    department = Department.objects.all()
    session = Session.objects.all()

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        department_id = request.POST.get('department_id')
        session_id = request.POST.get('session_id')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email Is Already Taken')
            return redirect('add_staff')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username Is Already Taken')
            return redirect('add_staff')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=3
            )
            user.set_password(password)
            user.save()

            department = Department.objects.get(id=department_id)
            session = Session.objects.get(id=session_id)

            staff = Staff(
                admin=user,
                address=address,
                session_id=session,
                department_id=department,
                gender=gender,
            )
            staff.save()
            messages.success(request, user.first_name + "  " + user.last_name + " Are Successfully Added !")
            return redirect('add_staff')

    context = {
        'department': department,
        'session': session,
    }

    return render(request, 'Hod/add_staff.html', context)


@login_required(login_url='/')
def VIEW_STAFF(request):
    staff = Staff.objects.all()

    context = {
        'staff': staff,
    }
    return render(request, 'Hod/view_staff.html', context)


@login_required(login_url='/')
def EDIT_STAFF(request, id):
    staff = Staff.objects.filter(id=id)
    department = Department.objects.all()
    session = Session.objects.all()

    context = {
        'staff': staff,
        'department': department,
        'session': session,
    }
    return render(request, 'Hod/edit_staff.html', context)


@login_required(login_url='/')
def UPDATE_STAFF(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        department_id = request.POST.get('department_id')
        session_id = request.POST.get('session_id')

        user = CustomUser.objects.get(id=staff_id)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()

        staff = Staff.objects.get(admin=staff_id)
        staff.address = address
        staff.gender = gender

        department = Department.objects.get(id=department_id)
        staff.department_id = department

        session = Session.objects.get(id=session_id)
        staff.session_id = session

        staff.save()
        messages.success(request, 'Record Are Successfully Updated !')
        return redirect('view_staff')

    return render(request, 'Hod/edit_staff.html')


@login_required(login_url='/')
def DELETE_STAFF(request, admin):
    staff = CustomUser.objects.get(id=admin)
    staff.delete()
    messages.success(request, 'Record Are Successfully Deleted !')
    return redirect('view_staff')


# Incharge All Function
@login_required(login_url='/')
def ADD_INCHARGE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email Is Already Taken')
            return redirect('add_incharge')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username Is Already Taken')
            return redirect('add_incharge')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=2
            )
            user.set_password(password)
            user.save()

            incharge = Incharge(
                admin=user,
                address=address,
                gender=gender,
            )
            incharge.save()
            messages.success(request, user.first_name + "  " + user.last_name + " Are Successfully Added !")
            return redirect('add_incharge')

    context = {

    }

    return render(request, 'Hod/add_incharge.html', context)


@login_required(login_url='/')
def VIEW_INCHARGE(request):
    incharge = Incharge.objects.all()

    context = {
        'incharge': incharge,
    }
    return render(request, 'Hod/view_incharge.html', context)


# Sataff All Function
@login_required(login_url='/')
def EDIT_INCHARGE(request, id):
    incharge = Incharge.objects.filter(id=id)

    context = {
        'incharge': incharge,
    }
    return render(request, 'Hod/edit_incharge.html', context)


@login_required(login_url='/')
def UPDATE_INCHARGE(request):
    if request.method == "POST":
        incharge_id = request.POST.get('incharge_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        user = CustomUser.objects.get(id=incharge_id)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()

        incharge = Incharge.objects.get(admin=incharge_id)
        incharge.address = address
        incharge.gender = gender

        incharge.save()
        messages.success(request, 'Record Are Successfully Updated !')
        return redirect('view_incharge')

    return render(request, 'Hod/edit_incharge.html')


@login_required(login_url='/')
def DELETE_INCHARGE(request, admin):
    incharge = CustomUser.objects.get(id=admin)
    incharge.delete()
    messages.success(request, 'Record Are Successfully Deleted !')
    return redirect('view_incharge')


# Department All Function
@login_required(login_url='/')
def ADD_DEPARTMENT(request):
    if request.method == "POST":
        department_name = request.POST.get('department_name')

        department = Department(
            name=department_name,
        )
        department.save()
        messages.success(request, 'Department Are Successfully Created ')

        return redirect('add_department')

    return render(request, 'Hod/add_department.html')


@login_required(login_url='/')
def VIEW_DEPARTMENT(request):
    department = Department.objects.all()
    context = {
        'department': department,
    }
    return render(request, 'Hod/view_department.html', context)


@login_required(login_url='/')
def EDIT_DEPARTMENT(request, id):
    department = Department.objects.get(id=id)

    context = {
        'department': department,
    }

    return render(request, 'Hod/edit_department.html', context)


@login_required(login_url='/')
def UPDATE_DEPARTMENT(request):
    if request.method == "POST":
        name = request.POST.get('name')
        department_id = request.POST.get('department_id')

        department = Department.objects.get(id=department_id)
        department.name = name
        department.save()

        messages.success(request, 'Department Are Successfully Updated !')
        return redirect('view_department')

    return render(request, 'Hod/edit_department.html')


@login_required(login_url='/')
def DELETE_DEPARTMENT(request, id):
    department = Department.objects.get(id=id)
    department.delete()
    messages.success(request, 'Department are Successfully Deleted')

    return redirect('view_department')


# Session All Function
@login_required(login_url='/')
def ADD_SESSION(request):
    if request.method == "POST":
        session_start = request.POST.get('session_start')
        session_end = request.POST.get('session_end')

        session = Session(
            session_start = session_start,
            session_end = session_end
        )
        session.save()
        messages.success(request, 'Session Are Successfully Created ')

        return redirect('add_session')

    return render(request, 'Hod/add_session.html')


@login_required(login_url='/')
def VIEW_SESSION(request):
    session = Session.objects.all()

    context = {
        'session': session,
    }
    return render(request, 'Hod/view_session.html', context)


@login_required(login_url='/')
def EDIT_SESSION(request, id):
    session = Session.objects.filter(id=id)

    context = {
        'session': session,
    }

    return render(request, 'Hod/edit_session.html', context)


@login_required(login_url='/')
def UPDATE_SESSION(request):
    if request.method == "POST":
        session_id = request.POST.get('session_id')
        session_start = request.POST.get('session_start')
        session_end = request.POST.get('session_end')

        session = Session(
            id = session_id,
            session_start = session_start,
            session_end = session_end
        )

        session.save()

        messages.success(request, 'Session Are Successfully Updated !')
        return redirect('view_session')

    return render(request, 'Hod/edit_session.html')


@login_required(login_url='/')
def DELETE_SESSION(request, id):
    session = Session.objects.get(id=id)
    session.delete()
    messages.success(request, 'Session are Successfully Deleted')

    return redirect('view_session')


# section All Function
@login_required(login_url='/')
def ADD_SECTION(request):
    department = Department.objects.all()
    incharge = Incharge.objects.all()

    if request.method == "POST":
        section_name = request.POST.get('section_name')
        department_id = request.POST.get('department_id')
        incharge_id = request.POST.get('incharge_id')

        department = Department.objects.get(id=department_id)
        incharge = Incharge.objects.get(id=incharge_id)

        section = Section(
            name=section_name,
            department=department,
            incharge=incharge,
        )

        section.save()
        messages.success(request, 'Section Are Successfully Created ')
        return redirect('add_section')

    context = {
        'department': department,
        'incharge': incharge,
    }
    return render(request, 'Hod/add_section.html', context)

@login_required(login_url='/')
def VIEW_SECTION(request):
    section = Section.objects.all()
    context = {
        'section': section,
    }
    return render(request, 'Hod/view_section.html', context)

@login_required(login_url='/')
def EDIT_SECTION(request, id):
    section = Section.objects.get(id=id)
    department = Department.objects.all()
    incharge = Incharge.objects.all()

    context = {
        'section': section,
        'department': department,
        'incharge': incharge,
    }

    return render(request, 'Hod/edit_section.html', context)

@login_required(login_url='/')
def UPDATE_SECTION(request):
    if request.method == "POST":
        section_id = request.POST.get('section_id')
        section_name = request.POST.get('section_name')
        department_id = request.POST.get('department_id')
        incharge_id = request.POST.get('incharge_id')

        department = Department.objects.get(id=department_id)
        incharge = Incharge.objects.get(id=incharge_id)

        section = Section(
            id = section_id,
            name = section_name,
            department = department,
            incharge = incharge,
        )

        section.save()
        messages.success(request, 'Section Are Successfully Updated !')

        return redirect('view_section')

    return render(request, 'Hod/edit_section.html')

@login_required(login_url='/')
def DELETE_SECTION(request, id):
    section = Section.objects.get(id=id)
    section.delete()
    messages.success(request, 'section are Successfully Deleted')

    return redirect('view_section')


@login_required(login_url='/')
def SEND_INCHARGE_NOTIFICATION(request):
    incharge = Incharge.objects.all()
    see_notification = Incharge_Notification.objects.all().order_by('-id')[0:5]

    context = {
        'incharge': incharge,
        'see_notification': see_notification,
    }
    return render(request, 'Hod/incharge_notification.html', context)


@login_required(login_url='/')
def SAVE_INCHARGE_NOTIFICATION(request):
    if request.method == "POST":
        incharge_id = request.POST.get('incharge_id')
        message = request.POST.get('message')

        incharge = Incharge.objects.get(admin = incharge_id)
        notification = Incharge_Notification(
            incharge_id = incharge,
            message = message,
        )
        notification.save()
        messages.success(request, 'Notification are Successfully Sent')
        return redirect('send_incharge_notification')


@login_required(login_url='/')
def SEND_STAFF_NOTIFICATION(request):
    staff = Staff.objects.all()
    see_notification = Staff_Notification.objects.all().order_by('-id')[0:5]

    context = {
        'staff': staff,
        'see_notification': see_notification,
    }
    return render(request, 'Hod/staff_notification.html', context)


@login_required(login_url='/')
def SAVE_STAFF_NOTIFICATION(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        message = request.POST.get('message')

        staff = Staff.objects.get(admin = staff_id)
        notification = Staff_Notification(
            staff_id = staff,
            message = message,
        )
        notification.save()
        messages.success(request, 'Notification are Successfully Sent')
        return redirect('send_staff_notification')

@login_required(login_url='/')
def VIEW_INCHARGE_LEAVE(request):
    incharge_leave = Incharge_Leave.objects.all()

    context = {
        'incharge_leave': incharge_leave,
    }

    return render(request, 'Hod/incharge_leave.html', context)


def INCHARGE_LEAVE_SAVE(request):
    if request.method == "POST":
        leave_reason_id = request.POST.get('leave_reason_id')
        leave_comments = request.POST.get('leave_comments')

        leave_reason = Incharge_Leave.objects.get(id=leave_reason_id)
        leave_reason.leave_comments = leave_comments

        leave_reason.save()

    return redirect('view_incharge_leave')


@login_required(login_url='/')
def INCHARGE_LEAVE_APPLICATION_PDF(request):
    incharge_leave = Incharge_Leave.objects.all()

    template_path = 'Hod/incharge_leave_application_pdf.html'

    context = {
        'incharge_leave': incharge_leave
    }

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="incharge_leave_application.pdf"'

    template = get_template(template_path)

    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')

    return response


@login_required(login_url='/')
def APPROVE_INCHARGE_LEAVE(request, id):
    leave = Incharge_Leave.objects.get(id = id)
    leave.hod_action = 1
    leave.save()
    return redirect('view_incharge_leave')


@login_required(login_url='/')
def DISAPPROVE_INCHARGE_LEAVE(request, id):
    leave = Incharge_Leave.objects.get(id=id)
    leave.hod_action = 2
    leave.save()
    return redirect('view_incharge_leave')


@login_required(login_url='/')
def VIEW_STAFF_LEAVE(request):
    staff_leave = Staff_Leave.objects.all()

    context = {
        'staff_leave': staff_leave,
    }

    return render(request, 'Hod/staff_leave.html', context)


def STAFF_LEAVE_SAVE(request):
    if request.method == "POST":
        leave_reason_id = request.POST.get('leave_reason_id')
        leave_comments = request.POST.get('leave_comments')

        leave_reason = Staff_Leave.objects.get(id=leave_reason_id)
        leave_reason.leave_comments = leave_comments

        leave_reason.save()

    return redirect('view_staff_leave')


@login_required(login_url='/')
def STAFF_LEAVE_APPLICATION_PDF(request):
    staff_leave = Staff_Leave.objects.all()

    template_path = 'Hod/staff_leave_application_pdf.html'

    context = {
        'staff_leave': staff_leave
    }

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="staff_leave_application.pdf"'

    template = get_template(template_path)

    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')

    return response


@login_required(login_url='/')
def APPROVE_STAFF_LEAVE(request, id):
    leave = Staff_Leave.objects.get(id = id)
    leave.hod_action = 1
    leave.save()
    return redirect('view_staff_leave')


@login_required(login_url='/')
def DISAPPROVE_STAFF_LEAVE(request, id):
    leave = Staff_Leave.objects.get(id=id)
    leave.hod_action = 2
    leave.save()
    return redirect('view_staff_leave')


@login_required(login_url='/')
def HOD_INCHARGE_FEEDBACK(request):
    feedback = Incharge_Feedback.objects.all()
    feedback_history = Incharge_Feedback.objects.all().order_by('-id')[0:5]

    context = {
        'feedback': feedback,
        'hod_feedback_history': feedback_history,
    }

    return render(request, 'Hod/incharge_feedback.html', context)


@login_required(login_url='/')
def HOD_INCHARGE_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')

        feedback = Incharge_Feedback.objects.get(id = feedback_id)
        feedback.feedback_reply = feedback_reply

        feedback.status = 1
        feedback.save()

        return redirect('hod_incharge_feedback')


@login_required(login_url='/')
def HOD_STAFF_FEEDBACK(request):
    feedback = Staff_Feedback.objects.all()
    feedback_history = Staff_Feedback.objects.all().order_by('-id')[0:5]

    context = {
        'feedback': feedback,
        'hod_feedback_history': feedback_history,
    }

    return render(request, 'Hod/staff_feedback.html', context)


@login_required(login_url='/')
def HOD_STAFF_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')

        feedback = Staff_Feedback.objects.get(id = feedback_id)
        feedback.feedback_reply = feedback_reply

        feedback.status = 1
        feedback.save()

        return redirect('hod_staff_feedback')


def HOD_STAFF_TAKE_ATTENDANCE(request):

    section = Section.objects.all()
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

    return render(request, 'Hod/staff_take_attendance.html', context)


def HOD_STAFF_SAVE_ATTENDANCE(request):
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

    return redirect('hod_staff_take_attendance')


def HOD_STAFF_VIEW_ATTENDANCE(request):

    section = Section.objects.all()
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

    return render(request, 'Hod/staff_view_attendance.html', context)


def HOD_INCHARGE_TAKE_ATTENDANCE(request):

    section = Section.objects.all()
    session = Session.objects.all()

    action = request.GET.get('action')

    incharges = None
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
                incharges = Incharge.objects.all()

    context = {
        'action': action,
        'section': section,
        'session': session,
        'get_section': get_section,
        'get_session': get_session,
        'incharges': incharges,
    }

    return render(request, 'Hod/incharge_take_attendance.html', context)


def HOD_INCHARGE_SAVE_ATTENDANCE(request):
    if request.method == "POST":
        section_id = request.POST.get('section_id')
        session_id = request.POST.get('session_id')
        incharge_attendance_date = request.POST.get('incharge_attendance_date')
        incharge_id = request.POST.getlist('incharge_id')

        get_section = Section.objects.get(id=section_id)
        get_session = Session.objects.get(id=session_id)

        incharge_attendance = Incharge_Attendance(
            section_id=get_section,
            incharge_attendance_date=incharge_attendance_date,
            session_id=get_session,
        )
        incharge_attendance.save()

        for i in incharge_id:
            stud_id = i
            int_stud = int(stud_id)

            p_incharges = Incharge.objects.get(id=int_stud)

            incharge_attendance_report = Incharge_Attendance_Report(
                incharge_id=p_incharges,
                incharge_attendance_id=incharge_attendance,
            )
            incharge_attendance_report.save()

    return redirect('hod_incharge_take_attendance')


def HOD_INCHARGE_VIEW_ATTENDANCE(request):

    section = Section.objects.all()
    session = Session.objects.all()

    action = request.GET.get('action')

    get_section = None
    get_session = None
    incharge_attendance_date = None
    incharge_attendance_report = None

    if action is not None:
        if request.method == "POST":
            section_id = request.POST.get('section_id')
            session_id = request.POST.get('session_id')
            incharge_attendance_date = request.POST.get('incharge_attendance_date')

            get_section = Section.objects.get(id=section_id)
            get_session = Session.objects.get(id=session_id)
            incharge_attendance = Incharge_Attendance.objects.filter(section_id=get_section, incharge_attendance_date=incharge_attendance_date, )
            for i in incharge_attendance:
                incharge_attendance_id = i.id
                incharge_attendance_report = Incharge_Attendance_Report.objects.filter(incharge_attendance_id=incharge_attendance_id)

    context = {
        'section': section,
        'session': session,
        'action': action,
        'get_section': get_section,
        'get_session': get_session,
        'incharge_attendance_date': incharge_attendance_date,
        'incharge_attendance_report': incharge_attendance_report,
    }

    return render(request, 'Hod/incharge_view_attendance.html', context)

