from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def happ(request):
    return HttpResponse('Hey i am from happ')
