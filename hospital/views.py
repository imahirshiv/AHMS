from django.shortcuts import render,redirect
from django.http import HttpResponse


def BASE(request):
    return render (request,'base.html')