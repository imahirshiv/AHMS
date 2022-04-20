from django.urls import path
from patients import views

urlpatterns = [
    path('patient/',views.patient),
]
