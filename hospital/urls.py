from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from hospital import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.BASE,name='base'),
    path('account/',include('accounts.urls')),
    path('doctor/',include('doctors.urls')),
    path('happ/',include('hospitalapp.urls')),
    path('patient/',include('patients.urls')),
    


]
