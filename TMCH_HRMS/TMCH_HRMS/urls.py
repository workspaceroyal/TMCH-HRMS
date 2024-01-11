from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views, Hod_Views, Staff_Views, Student_Views

urlpatterns = [
                path('admin/', admin.site.urls),
                path('base/', views.BASE, name='base'),

                # Login Path
                path('', views.LOGIN, name='login'),
                path('doLogin',views.doLogin,name='doLogin'),

                # Logout Path
                path('doLogout',views.doLogout,name='logout'),

                # Profile Path
                path('Profile',views.PROFILE,name='profile'),
                path('Profile/update',views.PROFILE_UPDATE,name='profile_update'),


                # Hod Panel Path
                path('Hod/Home',Hod_Views.HOME,name='hod_home'),

                path('Hod/Student/Add',Hod_Views.ADD_STUDENT,name='add_student'),
                path('Hod/Student/View',Hod_Views.VIEW_STUDENT,name='view_student'),
                path('Hod/Student/Edit/<str:id>',Hod_Views.EDIT_STUDENT,name='edit_student'),
                path('Hod/Student/Update',Hod_Views.UPDATE_STUDENT,name='update_student'),
                path('Hod/Student/Delete/<str:admin>',Hod_Views.DELETE_STUDENT,name='delete_student'),

                path('Hod/Staff/Add',Hod_Views.ADD_STAFF,name='add_staff'),
                path('Hod/Staff/View',Hod_Views.VIEW_STAFF,name='view_staff'),
                path('Hod/Staff/Edit/<str:id>',Hod_Views.EDIT_STAFF,name='edit_staff'),
                path('Hod/Staff/Update',Hod_Views.UPDATE_STAFF,name='update_staff'),
                path('Hod/Staff/Delete/<str:admin>',Hod_Views.DELETE_STAFF,name='delete_staff'),

                path('Hod/Course/Add',Hod_Views.ADD_COURSE,name='add_course'),
                path('Hod/Course/View',Hod_Views.VIEW_COURSE,name='view_course'),
                path('Hod/Course/Edit/<str:id>',Hod_Views.EDIT_COURSE,name='edit_course'),
                path('Hod/Course/Update',Hod_Views.UPDATE_COURSE,name='update_course'),
                path('Hod/Course/Delete/<str:id>',Hod_Views.DELETE_COURSE,name='delete_course'),

                path('Hod/Session/Add',Hod_Views.ADD_SESSION,name='add_session'),
                path('Hod/Session/View',Hod_Views.VIEW_SESSION,name='view_session'),
                path('Hod/Session/Edit/<str:id>',Hod_Views.EDIT_SESSION,name='edit_session'),
                path('Hod/Session/Update',Hod_Views.UPDATE_SESSION,name='update_session'),
                path('Hod/Session/Delete/<str:id>',Hod_Views.DELETE_SESSION,name='delete_session'),

                path('Hod/Subject/Add',Hod_Views.ADD_SUBJECT,name='add_subject'),
                path('Hod/Subject/View',Hod_Views.VIEW_SUBJECT,name='view_subject'),
                path('Hod/Subject/Edit/<str:id>',Hod_Views.EDIT_SUBJECT,name='edit_subject'),
                path('Hod/Subject/Update',Hod_Views.UPDATE_SUBJECT,name='update_subject'),
                path('Hod/Subject/Delete/<str:id>',Hod_Views.DELETE_SUBJECT,name='delete_subject'),

                path('Hod/Staff/Send_Notification', Hod_Views.SEND_STAFF_NOTIFICATION,name='send_staff_notification'),
                path('Hod/Staff/Save_Notification', Hod_Views.SAVE_STAFF_NOTIFICATION,name='save_staff_notification'),

                path('Hod/Staff/View_Leave', Hod_Views.VIEW_STAFF_LEAVE,name='view_staff_leave'),
                path('Hod/Staff/Approve_Leave/<str:id>', Hod_Views.APPROVE_STAFF_LEAVE,name='approve_staff_leave'),
                path('Hod/Staff/Disapprove_Leave/<str:id>', Hod_Views.DISAPPROVE_STAFF_LEAVE, name='disapprove_staff_leave'),

                path('Hod/Staff/Feedback', Hod_Views.HOD_STAFF_FEEDBACK,name='hod_staff_feedback'),
                path('Hod/Staff/Feedback/Save', Hod_Views.HOD_STAFF_FEEDBACK_SAVE, name='hod_staff_feedback_save'),

                  # Staff Panel Path
                path('Staff/Home',Staff_Views.HOME,name='staff_home'),

                path('Staff/Notifications',Staff_Views.NOTIFICATIONS,name='notifications'),
                path('Staff/Notification_Marking/<str:status>',Staff_Views.NOTIFICATION_MARKING,name='notification_marking'),

                path('Staff/Apply_Leave_Full_Day',Staff_Views.APPLY_STAFF_LEAVE_FULL_DAY,name='apply_staff_leave_full_day'),
                path('Staff/Apply_Leave_Short_Time',Staff_Views.APPLY_STAFF_LEAVE_SHORT_TIME,name='apply_staff_leave_short_time'),
                path('Staff/Save_Apply_Leave',Staff_Views.SAVE_APPLY_STAFF_LEAVE,name='save_apply_staff_leave'),

                path('Staff/Feedback',Staff_Views.STAFF_FEEDBACK,name='staff_feedback'),
                path('Staff/Feedback/Save', Staff_Views.STAFF_FEEDBACK_SAVE, name='staff_feedback_save'),

                path('Staff/Take_Attendance', Staff_Views.STAFF_TAKE_ATTENDANCE, name='staff_take_attendance'),

                # path('Staff/Student/Add',Staff_Views.ADD_STUDENT,name='add_student'),
                # path('Staff/Student/View',Staff_Views.VIEW_STUDENT,name='view_student'),
                # path('Staff/Student/Edit/<str:id>',Staff_Views.EDIT_STUDENT,name='edit_student'),
                # path('Staff/Student/Update',Staff_Views.UPDATE_STUDENT,name='update_student'),
                # path('Staff/Student/Delete/<str:admin>',Staff_Views.DELETE_STUDENT,name='delete_student'),
                #
                # path('Staff/Staff/Add',Staff_Views.ADD_STAFF,name='add_staff'),
                # path('Staff/Staff/View',Staff_Views.VIEW_STAFF,name='view_staff'),
                # path('Staff/Staff/Edit/<str:id>',Staff_Views.EDIT_STAFF,name='edit_staff'),
                # path('Staff/Staff/Update',Staff_Views.UPDATE_STAFF,name='update_staff'),
                # path('Staff/Staff/Delete/<str:admin>',Staff_Views.DELETE_STAFF,name='delete_staff'),
                #
                # path('Staff/Course/Add',Staff_Views.ADD_COURSE,name='add_course'),
                # path('Staff/Course/View',Staff_Views.VIEW_COURSE,name='view_course'),
                # path('Staff/Course/Edit/<str:id>',Staff_Views.EDIT_COURSE,name='edit_course'),
                # path('Staff/Course/Update',Staff_Views.UPDATE_COURSE,name='update_course'),
                # path('Staff/Course/Delete/<str:id>',Staff_Views.DELETE_COURSE,name='delete_course'),
                #
                # path('Staff/Session/Add',Staff_Views.ADD_SESSION,name='add_session'),
                # path('Staff/Session/View',Staff_Views.VIEW_SESSION,name='view_session'),
                # path('Staff/Session/Edit/<str:id>',Staff_Views.EDIT_SESSION,name='edit_session'),
                # path('Staff/Session/Update',Staff_Views.UPDATE_SESSION,name='update_session'),
                # path('Staff/Session/Delete/<str:id>',Staff_Views.DELETE_SESSION,name='delete_session'),
                #
                # path('Staff/Subject/Add',Staff_Views.ADD_SUBJECT,name='add_subject'),
                # path('Staff/Subject/View',Staff_Views.VIEW_SUBJECT,name='view_subject'),
                # path('Staff/Subject/Edit/<str:id>',Staff_Views.EDIT_SUBJECT,name='edit_subject'),
                # path('Staff/Subject/Update',Staff_Views.UPDATE_SUBJECT,name='update_subject'),
                # path('Staff/Subject/Delete/<str:id>',Staff_Views.DELETE_SUBJECT,name='delete_subject'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
