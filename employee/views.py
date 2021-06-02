from django.shortcuts import render,redirect
from django.views.generic import ListView
# from django.contrib.auth.decorators import login_required 

def login(request):
    return render(request, 'employee/login.html')

# @login_required
# def home(request):
#     return render(request, 'employee/homepage.html')