from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views, Hod_Views, Incharge_Views, Staff_Views

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

                path('Hod/Staff/Add',Hod_Views.ADD_STAFF,name='add_staff'),
                path('Hod/Staff/View',Hod_Views.VIEW_STAFF,name='view_staff'),
                path('Hod/Staff/Edit/<str:id>',Hod_Views.EDIT_STAFF,name='edit_staff'),
                path('Hod/Staff/Update',Hod_Views.UPDATE_STAFF,name='update_staff'),
                path('Hod/Staff/Delete/<str:admin>',Hod_Views.DELETE_STAFF,name='delete_staff'),

                path('Hod/Incharge/Add',Hod_Views.ADD_INCHARGE,name='add_incharge'),
                path('Hod/Incharge/View',Hod_Views.VIEW_INCHARGE,name='view_incharge'),
                path('Hod/Incharge/Edit/<str:id>',Hod_Views.EDIT_INCHARGE,name='edit_incharge'),
                path('Hod/Incharge/Update',Hod_Views.UPDATE_INCHARGE,name='update_incharge'),
                path('Hod/Incharge/Delete/<str:admin>',Hod_Views.DELETE_INCHARGE,name='delete_incharge'),

                path('Hod/Department/Add',Hod_Views.ADD_DEPARTMENT,name='add_department'),
                path('Hod/Department/View',Hod_Views.VIEW_DEPARTMENT,name='view_department'),
                path('Hod/Department/Edit/<str:id>',Hod_Views.EDIT_DEPARTMENT,name='edit_department'),
                path('Hod/Department/Update',Hod_Views.UPDATE_DEPARTMENT,name='update_department'),
                path('Hod/Department/Delete/<str:id>',Hod_Views.DELETE_DEPARTMENT,name='delete_department'),

                path('Hod/Session/Add',Hod_Views.ADD_SESSION,name='add_session'),
                path('Hod/Session/View',Hod_Views.VIEW_SESSION,name='view_session'),
                path('Hod/Session/Edit/<str:id>',Hod_Views.EDIT_SESSION,name='edit_session'),
                path('Hod/Session/Update',Hod_Views.UPDATE_SESSION,name='update_session'),
                path('Hod/Session/Delete/<str:id>',Hod_Views.DELETE_SESSION,name='delete_session'),

                path('Hod/section/Add',Hod_Views.ADD_SECTION,name='add_section'),
                path('Hod/section/View',Hod_Views.VIEW_SECTION,name='view_section'),
                path('Hod/section/Edit/<str:id>',Hod_Views.EDIT_SECTION,name='edit_section'),
                path('Hod/section/Update',Hod_Views.UPDATE_SECTION,name='update_section'),
                path('Hod/section/Delete/<str:id>',Hod_Views.DELETE_SECTION,name='delete_section'),

                path('Hod/Incharge_Send_Notification', Hod_Views.SEND_INCHARGE_NOTIFICATION,name='send_incharge_notification'),
                path('Hod/Incharge_Save_Notification', Hod_Views.SAVE_INCHARGE_NOTIFICATION,name='save_incharge_notification'),

                path('Hod/Staff_Send_Notification', Hod_Views.SEND_STAFF_NOTIFICATION,name='send_staff_notification'),
                path('Hod/Staff_Save_Notification', Hod_Views.SAVE_STAFF_NOTIFICATION,name='save_staff_notification'),

                  path('Hod/Incharge_Leave_View', Hod_Views.VIEW_INCHARGE_LEAVE, name='view_incharge_leave'),
                  path('Hod/Incharge_Leave_Save', Hod_Views.INCHARGE_LEAVE_SAVE, name='incharge_leave_save'),
                  path('Hod/Incharge_Leave_Approve/<str:id>', Hod_Views.APPROVE_INCHARGE_LEAVE, name='approve_incharge_leave'),
                  path('Hod/Incharge_Leave_Disapprove/<str:id>', Hod_Views.DISAPPROVE_INCHARGE_LEAVE, name='disapprove_incharge_leave'),
                  path('Hod/Incharge_Leave_Application_PDF', Hod_Views.INCHARGE_LEAVE_APPLICATION_PDF, name='incharge_leave_application_pdf'),

                path('Hod/Staff_Leave_View', Hod_Views.VIEW_STAFF_LEAVE, name='view_staff_leave'),
                path('Hod/Staff_Leave_Save', Hod_Views.STAFF_LEAVE_SAVE, name='staff_leave_save'),
                path('Hod/Staff_Leave_Approve/<str:id>', Hod_Views.APPROVE_STAFF_LEAVE, name='approve_staff_leave'),
                path('Hod/Staff_Leave_Disapprove/<str:id>', Hod_Views.DISAPPROVE_STAFF_LEAVE, name='disapprove_staff_leave'),
                path('Hod/Staff_Leave_Application_PDF', Hod_Views.STAFF_LEAVE_APPLICATION_PDF, name='staff_leave_application_pdf'),

                path('Hod/Incharge_Feedback', Hod_Views.HOD_INCHARGE_FEEDBACK,name='hod_incharge_feedback'),
                path('Hod/Incharge_Feedback/Save', Hod_Views.HOD_INCHARGE_FEEDBACK_SAVE, name='hod_incharge_feedback_save'),

                path('Hod/Staff_Feedback', Hod_Views.HOD_STAFF_FEEDBACK,name='hod_staff_feedback'),
                path('Hod/Staff_Feedback/Save', Hod_Views.HOD_STAFF_FEEDBACK_SAVE, name='hod_staff_feedback_save'),

                path('Hod/Staff_Take_Attendance', Hod_Views.HOD_STAFF_TAKE_ATTENDANCE,name='hod_staff_take_attendance'),
                path('Hod/Staff_Save_Attendance', Hod_Views.HOD_STAFF_SAVE_ATTENDANCE, name='hod_staff_save_attendance'),
                path('Hod/Staff_View_Attendance', Hod_Views.HOD_STAFF_VIEW_ATTENDANCE, name='hod_staff_view_attendance'),

                path('Hod/Incharge_Take_Attendance', Hod_Views.HOD_INCHARGE_TAKE_ATTENDANCE, name='hod_incharge_take_attendance'),
                path('Hod/Incharge_Save_Attendance', Hod_Views.HOD_INCHARGE_SAVE_ATTENDANCE, name='hod_incharge_save_attendance'),
                path('Hod/Incharge_View_Attendance', Hod_Views.HOD_INCHARGE_VIEW_ATTENDANCE, name='hod_incharge_view_attendance'),

                # Incharge Panel Path
                path('Incharge/Home',Incharge_Views.HOME,name='incharge_home'),

                path('Incharge/Notifications',Incharge_Views.NOTIFICATIONS,name='incharge_notifications'),
                path('Incharge/Notification_Marking/<str:status>',Incharge_Views.NOTIFICATION_MARKING,name='incharge_notification_marking'),

                path('Incharge/Staff_Send_Notification', Incharge_Views.SEND_STAFF_NOTIFICATION,name='incharge_send_staff_notification'),
                path('Incharge/Staff_Save_Notification', Incharge_Views.SAVE_STAFF_NOTIFICATION,name='incharge_save_staff_notification'),

                path('Incharge/Apply_Leave_Full_Day', Incharge_Views.APPLY_INCHARGE_LEAVE_FULL_DAY, name='apply_incharge_leave_full_day'),
                path('Incharge/Apply_Leave_Short_Time', Incharge_Views.APPLY_INCHARGE_LEAVE_SHORT_TIME, name='apply_incharge_leave_short_time'),
                path('Incharge/Save_Apply_Leave', Incharge_Views.SAVE_APPLY_INCHARGE_LEAVE, name='save_apply_incharge_leave'),

                path('Incharge/Feedback',Incharge_Views.INCHARGE_FEEDBACK,name='incharge_feedback'),
                path('Incharge/Feedback/Save', Incharge_Views.INCHARGE_FEEDBACK_SAVE, name='incharge_feedback_save'),

                path('Incharge/Staff_Feedback', Incharge_Views.INCHARGE_STAFF_FEEDBACK, name='incharge_staff_feedback'),
                path('Incharge/Staff_Feedback/Save', Incharge_Views.INCHARGE_STAFF_FEEDBACK_SAVE, name='incharge_staff_feedback_save'),

                # path('Incharge/Take_Attendance', Incharge_Views.INCHARGE_TAKE_ATTENDANCE, name='incharge_take_attendance'),
                path('Incharge/Staff_Take_Attendance', Incharge_Views.INCHARGE_STAFF_TAKE_ATTENDANCE, name='incharge_staff_take_attendance'),
                path('Incharge/Staff_Save_Attendance', Incharge_Views.INCHARGE_STAFF_SAVE_ATTENDANCE, name='incharge_staff_save_attendance'),
                path('Incharge/Staff_View_Attendance', Incharge_Views.INCHARGE_STAFF_VIEW_ATTENDANCE, name='incharge_staff_view_attendance'),

                path('Incharge/Incharge_View_Attendance', Incharge_Views.INCHARGE_VIEW_ATTENDANCE, name='incharge_view_attendance'),

                path('Incharge/Staff_Leave_View', Incharge_Views.INCHARGE_VIEW_STAFF_LEAVE, name='incharge_view_staff_leave'),
                path('Incharge/Staff_Leave_Save', Incharge_Views.INCHARGE_STAFF_LEAVE_SAVE, name='incharge_staff_leave_save'),
                path('Incharge/Staff_Approve_Leave/<str:id>', Incharge_Views.INCHARGE_APPROVE_STAFF_LEAVE, name='incharge_approve_staff_leave'),
                path('Incharge/Staff_Disapprove_Leave/<str:id>', Incharge_Views.INCHARGE_DISAPPROVE_STAFF_LEAVE, name='incharge_disapprove_staff_leave'),
                path('Incharge/Staff_Leave_Application_PDF', Incharge_Views.INCHARGE_STAFF_LEAVE_APPLICATION_PDF, name='incharge_staff_leave_application_pdf'),



                # Staff Panel Path
                path('Staff/Home',Staff_Views.HOME,name='staff_home'),

                path('Staff/Notifications', Staff_Views.NOTIFICATIONS, name='staff_notifications'),
                path('Staff/Notification_Marking/<str:status>', Staff_Views.NOTIFICATION_MARKING, name='staff_notification_marking'),

                path('Staff/Incharge_Notifications', Staff_Views.INCHARGE_NOTIFICATIONS, name='incharge_staff_notifications'),
                path('Staff/Incharge_Notification_Marking/<str:status>', Staff_Views.INCHARGE_NOTIFICATION_MARKING, name='incharge_staff_notification_marking'),

                path('Staff/Apply_Leave_Full_Day', Staff_Views.APPLY_STAFF_LEAVE_FULL_DAY, name='apply_staff_leave_full_day'),
                path('Staff/Apply_Leave_Short_Time', Staff_Views.APPLY_STAFF_LEAVE_SHORT_TIME, name='apply_staff_leave_short_time'),
                path('Staff/Save_Apply_Leave', Staff_Views.SAVE_APPLY_STAFF_LEAVE, name='save_apply_staff_leave'),

                path('Staff/Feedback', Staff_Views.STAFF_FEEDBACK, name='staff_feedback'),
                path('Staff/Feedback/Save', Staff_Views.STAFF_FEEDBACK_SAVE, name='staff_feedback_save'),

                path('Staff/Feedback_Incharge', Staff_Views.STAFF_FEEDBACK_INCHARGE, name='staff_feedback_incharge'),
                path('Staff/Feedback_Incharge/Save', Staff_Views.STAFF_FEEDBACK_INCHARGE_SAVE, name='staff_feedback_incharge_save'),

                path('Staff/View_Attendance', Staff_Views.STAFF_VIEW_ATTENDANCE, name='staff_view_attendance'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
