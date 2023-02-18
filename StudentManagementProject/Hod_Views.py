from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from myApp.models import Course, SessionYear, CustomUser, Student, Staff, Subject
from django.contrib import messages


@login_required(login_url='/')
def home(request):
  return render(request, 'Hod/home.html')


@login_required(login_url='/')
def add_student(request):
  course = Course.objects.all()
  session_year = SessionYear.objects.all()
  
  if request.method == "POST":
    profile_pic = request.FILES.get("profile_pic")
    f_name = request.POST.get("f_name")
    l_name = request.POST.get("l_name")
    username = request.POST.get("username")
    password = request.POST.get("password")
    email = request.POST.get("email")
    gender = request.POST.get("gender")
    course_id = request.POST.get("course_id")
    session_year_id = request.POST.get("session_year_id")
    address = request.POST.get("address")
    
    if CustomUser.objects.filter(email=email).exists():
      messages.warning(request, "Email is already exist")
      return redirect('add_student')
    if CustomUser.objects.filter(username=username).exists():
      messages.warning(request, "Username is already exist")
      return redirect('add_student')
    else:
      user = CustomUser(
        first_name=f_name,
        last_name=l_name,
        username=username,
        email=email,
        profile_Pic=profile_pic,
        user_type=3,
      )
      user.set_password(password)
      user.save()
      
      # add course model to other model
      course_add = Course.objects.get(id=course_id)
      session_year_add = SessionYear.objects.get(id=session_year_id)
      student = Student(
        admin=user,
        address=address,
        session_year_id=session_year_add,
        course_id=course_add,
        gender=gender,
      )
      
      student.save()
      messages.success(request, user.first_name + " " + user.last_name + " added successfully")
      return redirect('add_student')
  
  context = {'courses': course, 'session_years': session_year}
  return render(request, "Hod/add_student.html", context)


@login_required(login_url='/')
def view_student(request):
  student = Student.objects.all()
  return render(request, 'Hod/view_student.html', {"students": student})


@login_required(login_url='/')
def edit_student(request, id):
  course = Course.objects.all()
  sessions = SessionYear.objects.all()
  student = Student.objects.filter(id=id)
  context = {
    'students': student,
    'courses': course,
    'session_years': sessions,
  }
  return render(request, 'Hod/edit_student.html', context)


@login_required(login_url='/')
def update_student(request):
  if request.method == "POST":
    student_id = request.POST.get('student_id')
    profile_pic = request.FILES.get('profile_pic')
    f_name = request.POST.get('f_name')
    l_name = request.POST.get('l_name')
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    gender = request.POST.get('gender')
    course_id = request.POST.get('course_id')
    session_id = request.POST.get('session_year_id')
    address = request.POST.get('address')
    
    user = CustomUser.objects.get(id=student_id)
    
    user.first_name = f_name
    user.last_name = l_name
    user.username = username
    user.email = email
    
    if profile_pic is not None:
      user.profile_Pic = profile_pic
    if password is not None or password is not "":
      user.set_password = password
    user.save()
    
    student = Student.objects.get(admin=student_id)
    student.admin = user
    student.gender = gender
    student.address = address
    
    course_update_id = Course.objects.get(id=course_id)
    student.course_id = course_update_id
    
    session_update_id = SessionYear.objects.get(id=session_id)
    student.session_year_id = session_update_id
    
    student.save()
    messages.success(request, user.first_name + " " + user.last_name + "'s data updated successfully")
    return redirect('view_student')
  return render(request, 'Hod/view_student.html')


@login_required(login_url='/')
def delete_student(request, admin):
  student = CustomUser.objects.get(id=admin)
  student.delete()
  messages.success(request, "Data deleted successfully")
  return redirect('view_student')


@login_required(login_url='/')
def add_course(request):
  if request.method == "POST":
    course_add = request.POST.get('course_name')
    if Course.objects.filter(course_name=course_add).exists():
      messages.warning(request, "Course already exits!!!")
      return redirect("add_course")
    else:
      course = Course(
        course_name=course_add
      )
      course.save()
      messages.success(request, course_add + " course added successfully")
  return render(request, 'Hod/add_course.html')


@login_required(login_url='/')
def view_course(request):
  course = Course.objects.all()
  context = {
    'courses': course
  }
  return render(request, "Hod/view_course.html", context)


@login_required(login_url='/')
def edit_course(request, id):
  course = Course.objects.get(id=id)
  context = {
    'courses': course,
  }
  return render(request, "Hod/edit_course.html", context)


@login_required(login_url='/')
def update_course(request):
  if request.method == "POST":
    course_edit = request.POST.get('course_name')
    course_edit_id = request.POST.get('course_id')
    
    course = Course.objects.get(id=course_edit_id)
    course.course_name = course_edit
    
    course.save()
    messages.success(request, "Course updated successfully")
    return redirect('view_course')
  return render(request, "Hod/edit_course.html")


@login_required(login_url='/')
def delete_course(request, id):
  course = Course.objects.get(id=id)
  course.delete()
  messages.success(request, "Course deleted successfully")
  return redirect('view_course')


@login_required(login_url='/')
def add_staff(request):
  if request.method == "POST":
    profile_pic = request.FILES.get("profile_pic")
    f_name = request.POST.get("f_name")
    l_name = request.POST.get("l_name")
    username = request.POST.get("username")
    password = request.POST.get("password")
    email = request.POST.get("email")
    gender = request.POST.get("gender")
    address = request.POST.get("address")
    
    if CustomUser.objects.filter(email=email).exists():
      messages.warning(request, "Email already exists.")
    if CustomUser.objects.filter(username=username).exists():
      messages.warning(request, "Username already exists.")
    
    user = CustomUser(
      first_name=f_name,
      last_name=l_name,
      username=username,
      email=email,
      profile_Pic=profile_pic,
      user_type=2,
    )
    user.set_password(password)
    user.save()
    
    staff = Staff(
      admin=user,
      gender=gender,
      address=address,
    )
    staff.save()
    messages.success(request, "Staff data added successfully")
    return redirect('add_staff')
  return render(request, "Hod/add_staff.html")


@login_required(login_url='/')
def view_staff(request):
  staff = Staff.objects.all()
  context = {
    'staffs': staff,
  }
  return render(request, 'Hod/view_staff.html', context)


@login_required(login_url='/')
def edit_staff(request, id):
  staff = Staff.objects.get(id=id)
  context = {
    "id": staff.admin.id,
    "username": staff.admin.username,
    "first_name": staff.admin.first_name,
    "last_name": staff.admin.last_name,
    "email": staff.admin.email,
    "gender": staff.gender,
    "address": staff.address,
  }
  return render(request, "Hod/edit_staff.html", context)


@login_required(login_url='/')
def update_staff(request):
  if request.method == "POST":
    profile_pic = request.FILES.get("profile_pic")
    staff_id = request.POST.get("staff_id")
    f_name = request.POST.get("f_name")
    l_name = request.POST.get("l_name")
    username = request.POST.get("username")
    password = request.POST.get("password")
    email = request.POST.get("email")
    gender = request.POST.get("gender")
    address = request.POST.get("address")
    print(staff_id)
    user = CustomUser.objects.get(id=staff_id)
    
    user.first_name = f_name
    user.last_name = l_name
    user.email = email
    user.username = username
    
    if profile_pic is not None:
      user.profile_Pic = profile_pic
    
    if password is not "" or password is not None:
      user.set_password(password)
    user.save()
    
    staff = Staff.objects.get(admin=staff_id)
    staff.gender = gender
    staff.address = address
    staff.save()
    messages.success(request, "Staff data updated successfully")
    return redirect('view_staff')
  else:
    messages.error(request, "Error")
    return redirect('edit_staff')


@login_required(login_url='/')
def delete_staff(request, id):
  user_staff = CustomUser.objects.get(id=id)
  user_staff.delete()
  return render(request, 'Hod/view_staff.html')


@login_required(login_url='/')
def add_subject(request):
  staffs = Staff.objects.all()
  courses = Course.objects.all()
  
  context = {
    'staffs': staffs,
    'courses': courses,
  }
  
  if request.method == "POST":
    subject_name = request.POST.get("subject_name")
    staff_id = request.POST.get("staff_id")
    course_id = request.POST.get("course_id")
    
    course = Course.objects.get(id=course_id)
    staff = Staff.objects.get(id=staff_id)
    
    subject = Subject(
      subject_name=subject_name,
      course=course,
      staff=staff,
    )
    subject.save()
    messages.success(request, "Subject data added successfully")
    return redirect('view_subject')
  
  return render(request, 'Hod/add_subject.html', context)


@login_required(login_url='/')
def view_subject(request):
  subject = Subject.objects.all()
  context = {
    "subjects": subject,
  }
  return render(request, 'Hod/view_subject.html', context)


@login_required(login_url='/')
def edit_subject(request, id):
  subject = Subject.objects.get(id=id)
  course = Course.objects.all()
  staff = Staff.objects.all()
  context = {
    "subjects": subject,
    "courses": course,
    "staffs": staff,
  }
  return render(request, 'Hod/edit_subject.html', context)


@login_required(login_url='/')
def update_subject(request):
  if request.method == "POST":
    subject_id = request.POST.get("subject_id")
    subject_name = request.POST.get("subject_name")
    staff_id = request.POST.get("staff_id")
    course_id = request.POST.get("course_id")
    
    course = Course.objects.get(id=course_id)
    subject = Subject.objects.get(id=subject_id)
    staff = Staff.objects.get(id=staff_id)
    
    subject.subject_name = subject_name
    subject.course = course
    subject.staff = staff
    
    subject.save()
    messages.success(request, "Subject data updated successfully")
    return redirect('view_subject')
  
  return render(request, 'Hod/view_subject.html')


def delete_subject(request, id):
  subject = Subject.objects.get(id=id)
  subject.delete()
  messages.success(request, "Subject data deleted successfully")
  return redirect('view_subject')
