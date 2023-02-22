from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from myApp.models import Staff, StaffNotification, LeaveRequest


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
  return render(request, "Staff/view_staff_notification.html")


def notification_status(request, status):
  notification = StaffNotification.objects.get(id=status)
  notification.status = 1
  notification.save()
  return redirect('view_staff_notification')


def apply_leave(request):
  if request.method == "POST":
    staff_id = request.POST.get('staff_id')
    leave_date = request.POST.get('leave')
    from_date = request.POST.get('leave_from')
    to_date = request.POST.get('leave_to')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    
    staff_name = Staff.objects.get(admin=staff_id)
    print(leave_date, from_date, to_date, subject, message, staff_name)
    leave_request = LeaveRequest(
      staff_name=staff_name,
      leave_apply_date=leave_date,
      leave_from=from_date,
      leave_to=to_date,
      subject=subject,
      message=message,
    )
    leave_request.save()
    messages.success(request, "Leave applied successfully")
    return redirect('apply_leave')
  return render(request, "Staff/applyLeave.html")
