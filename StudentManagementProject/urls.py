
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views, Hod_Views, Staff_Views, Student_Views

urlpatterns = [
    path('admin', admin.site.urls),
    path('base', views.base, name='base'),

    #login url
    path('', views.Login, name='login'),
    path('doLogin/', views.do_login, name='doLogin'),
    path('doLogout/', views.do_logout, name='logout'),
    path('register/', views.register, name='register'),

    #hod url
    path('Hod/Home', Hod_Views.home, name='hod_home'),
    path('Hod/Student/add', Hod_Views.add_student, name='add_student'),
    path('Hod/Student/view', Hod_Views.view_student, name='view_student'),
    path('Hod/Student/edit/<str:id>', Hod_Views.edit_student, name='edit_student'),
    path('Hod/Student/update', Hod_Views.update_student, name='update_student'),
    path('Hod/Student/delete/<str:admin>', Hod_Views.delete_student, name='delete_student'),

    path('Hod/Staff/add', Hod_Views.add_staff, name='add_staff'),
    path('Hod/Staff/view', Hod_Views.view_staff, name='view_staff'),
    path('Hod/Staff/edit/<str:id>', Hod_Views.edit_staff, name='edit_staff'),
    path('Hod/Staff/update', Hod_Views.update_staff, name='update_staff'),
    path('Hod/Staff/delete/<str:id>', Hod_Views.delete_staff, name='delete_staff'),

    #hod course add
    path('Hod/Course/add', Hod_Views.add_course, name='add_course'),
    path('Hod/Course/view', Hod_Views.view_course, name='view_course'),
    path('Hod/Course/edit/<str:id>', Hod_Views.edit_course, name='edit_course'),
    path('Hod/Course/update', Hod_Views.update_course, name='update_course'),
    path('Hod/Course/delete/<str:id>', Hod_Views.delete_course, name='delete_course'),


    #staff url
    path('Staff/Home', Staff_Views.Home, name='staff_home'),

    #profile url
    path('profile', views.profile, name='profile'),
    path('profile/update', views.profile_update, name='profile_update'),


    #student url
    path('Student/Home', Student_Views.home, name='student_home'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
