from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def login(request):
    return render(request,'accounts/login.html')
def SignUpForm(request):
    return render(request,'accounts/signup.html')