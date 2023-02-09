from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def Home(request):
    return render(request, 'Staff/home.html')
