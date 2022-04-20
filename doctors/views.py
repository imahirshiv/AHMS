from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def doctor(request):
    return HttpResponse('Hey i am from doctor')