from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from myApp.models import Course, SessionYear, CustomUser, Student, Staff, Subject, StaffNotification
from django.contrib import messages

@login_required(login_url='/')
def home(request):
  staff = Staff.objects.filter(admin=request.user)
  for i in staff:
    staff_id = i.id
    notification_count = StaffNotification.objects.filter(staff_id=staff_id, status=0).count()
    context = {
      "notification_count": notification_count,
    }
    return render(request, 'Staff/home.html', context)


def view_staff_notification(request):
  staff = Staff.objects.filter(admin=request.user.id)
  for i in staff:
    staff_id = i.id
    notification = StaffNotification.objects.filter(staff_id=staff_id)
    notification_count = StaffNotification.objects.filter(staff_id=staff_id, status=0).count()
    context = {
      "notification": notification,
      "notification_count": notification_count,
    }
    return render(request, "Staff/view_staff_notification.html", context)


def notification_status(request, status):
  notification = StaffNotification.objects.get(id=status)
  notification.status = 1
  notification.save()
  return redirect('view_staff_notification')

