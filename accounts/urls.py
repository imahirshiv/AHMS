from django.urls import path
from accounts import views

urlpatterns = [
    path('login/',views.login),
    path('signup/',views.SignUpForm,name='signup'),
]
