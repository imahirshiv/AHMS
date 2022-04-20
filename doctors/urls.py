from django.urls import path
from doctors import views

urlpatterns = [
    path('doctor/',views.doctor),
]
