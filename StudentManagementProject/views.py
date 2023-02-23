from django.shortcuts import render, redirect
from myApp.EmailBackEnd import EmailBackEnd
from django.contrib.auth import login, logout
from django.contrib import messages
from myApp.models import CustomUser
from django.contrib.auth.decorators import login_required


@login_required(login_url="/")
def base(request):
  return render(request, 'base.html')


def login_page(request):
  return render(request, 'login.html')


def do_login(request):
  if request.method == "POST":
    user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
    if user is not None:
      login(request, user)
      user_type = user.user_type
      if user_type == '1':
        return redirect('hod_home')
      elif user_type == '2':
        return redirect("staff_home")
      elif user_type == '3':
        return redirect("student_home")
      else:
        messages.warning(request, "don't have account? create an account")
        return redirect('login')
    else:
      messages.error(request, "Invalid Credentials!!!")
      return redirect('login')
  return render(request, 'doLogin.html')


def do_logout(request):
  logout(request)
  return redirect('login')


def register(request):
  return render(request, 'register.html')


@login_required(login_url='/')
def profile(request):
  user = CustomUser.objects.get(id=request.user.id)
  context = {"user": user}
  
  return render(request, 'profile.html', context)


@login_required(login_url='/')
def profile_update(request):
  if request.method == 'POST':
    profile_pic = request.FILES.get('profile_pic')
    first_name = request.POST.get('f_name')
    last_name = request.POST.get('l_name')
    # email = request.POST.get('email')
    # username = request.POST.get('username')
    password = request.POST.get('password')
    try:
      custom_user = CustomUser.objects.get(id=request.user.id)
      if profile_pic is not None:
        custom_user.profile_Pic = profile_pic
      
      custom_user.first_name = first_name
      custom_user.last_name = last_name
      
      if password is not None and password is not "":
        custom_user.set_password(password)
      
      custom_user.save()
      messages.success(request, "Profile updated successfully!!!")
      return redirect('profile')
    except:
      messages.error(request, "Profile update failed!!!")
      return redirect('profile')
  return render(request, 'profile.html')
