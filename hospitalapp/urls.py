from django.urls import path
from hospitalapp import views

urlpatterns = [
    path('happ/',views.happ),
]
