from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class UserModel(UserAdmin):
    list_display = ['username', 'user_type']
    search_fields = ['username']
    list_per_page = 8
    

class StudentModel(admin.ModelAdmin):
    list_display = ['admin', 'gender', 'course_id']


class LeaveModel(admin.ModelAdmin):
    list_display = ['staff_name', 'subject']


admin.site.register(CustomUser, UserModel)
admin.site.register(Course)
admin.site.register(SessionYear)
admin.site.register(Student, StudentModel)
admin.site.register(Staff)
admin.site.register(Subject)
admin.site.register(StaffNotification)
admin.site.register(LeaveRequest, LeaveModel)
admin.site.register(StaffFeedback)
