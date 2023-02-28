from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views, Hod_Views, Staff_Views, Student_Views

urlpatterns = [
                path('admin', admin.site.urls),
                path('base', views.base, name='base'),
  
                # login url
                path('', views.login_page, name='login'),
                path('doLogin/', views.do_login, name='doLogin'),
                path('doLogout/', views.do_logout, name='logout'),
                path('register/', views.register, name='register'),
  
                ########################################################################################################
                # hod student url
                path('Hod/Home', Hod_Views.home, name='hod_home'),
                path('Hod/Student/add', Hod_Views.add_student, name='add_student'),
                path('Hod/Student/view', Hod_Views.view_student, name='view_student'),
                path('Hod/Student/edit/<str:id>', Hod_Views.edit_student, name='edit_student'),
                path('Hod/Student/update', Hod_Views.update_student, name='update_student'),
                path('Hod/Student/delete/<str:admin>', Hod_Views.delete_student, name='delete_student'),
  
                # Hod staff url
                path('Hod/Staff/add', Hod_Views.add_staff, name='add_staff'),
                path('Hod/Staff/view', Hod_Views.view_staff, name='view_staff'),
                path('Hod/Staff/edit/<str:id>', Hod_Views.edit_staff, name='edit_staff'),
                path('Hod/Staff/update', Hod_Views.update_staff, name='update_staff'),
                path('Hod/Staff/delete/<str:id>', Hod_Views.delete_staff, name='delete_staff'),
  
                # hod course url
                path('Hod/Course/add', Hod_Views.add_course, name='add_course'),
                path('Hod/Course/view', Hod_Views.view_course, name='view_course'),
                path('Hod/Course/edit/<str:id>', Hod_Views.edit_course, name='edit_course'),
                path('Hod/Course/update', Hod_Views.update_course, name='update_course'),
                path('Hod/Course/delete/<str:id>', Hod_Views.delete_course, name='delete_course'),
  
                # Hod subject url
                path('Hod/Subject/add', Hod_Views.add_subject, name='add_subject'),
                path('Hod/Subject/view', Hod_Views.view_subject, name='view_subject'),
                path('Hod/Subject/edit/<str:id>', Hod_Views.edit_subject, name='edit_subject'),
                path('Hod/Subject/update', Hod_Views.update_subject, name='update_subject'),
                path('Hod/Subject/delete/<str:id>', Hod_Views.delete_subject, name='delete_subject'),
  
                # Hod session url
                path('Hod/Session/add', Hod_Views.add_session, name='add_session'),
                path('Hod/Session/view', Hod_Views.view_session, name='view_session'),
                path('Hod/Session/edit/<str:id>', Hod_Views.edit_session, name='edit_session'),
                path('Hod/Session/update', Hod_Views.update_session, name='update_session'),
                path('Hod/Session/delete/<str:id>', Hod_Views.delete_session, name='delete_session'),
  
                path('Hod/Feedback/view', Hod_Views.view_staff_feedback, name='view_staff_feedback'),
                path('Hod/Feedback/reply', Hod_Views.reply_staff_feedback, name='reply_staff_feedback'),
  
                # Hod Notification url
                path('Hod/Notification/view', Hod_Views.view_notification, name='view_notification'),
                path('Hod/Notification/save', Hod_Views.save_notification, name='save_notification'),
                path('Hod/Notification/delete/<str:id>', Hod_Views.delete_notification, name='delete_notification'),
  
                # Hod Notification url
                path('Hod/Leave/staff', Hod_Views.view_staff_leave, name='view_staff_leave'),
                path('Hod/Leave/staff-accept/<str:id>', Hod_Views.accept_staff_leave, name='accept_staff_leave'),
                path('Hod/Leave/staff-decline/<str:id>', Hod_Views.decline_staff_leave, name='decline_staff_leave'),
                path('Hod/Leave/student', Hod_Views.view_student_leave, name='view_student_leave'),
  
                ########################################################################################################
                # staff notification url
                path('Staff/Home', Staff_Views.home, name='staff_home'),
  
                path('Staff/Notification/view', Staff_Views.view_staff_notification, name='view_staff_notification'),
                path('Staff/Notification/<str:status>', Staff_Views.notification_status, name='notification_status'),
                path('Staff/Leave/apply', Staff_Views.apply_leave, name='apply_leave'),
  
                ########################################################################################################
                # profile url
                path('profile', views.profile, name='profile'),
                path('profile/update', views.profile_update, name='profile_update'),
  
                ########################################################################################################
                # student url
                path('Student/Home', Student_Views.home, name='student_home'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
