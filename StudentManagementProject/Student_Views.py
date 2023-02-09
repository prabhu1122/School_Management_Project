from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from myApp.models import Student, CustomUser, Course, SessionYear


@login_required(login_url='/')
def home(request):
    student = Student.objects.all()
    context = {"students": student}
    return render(request, 'Student/home.html', context)
