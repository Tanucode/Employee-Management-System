from django.urls import path
from . views import *

urlpatterns = [
    path('login/',login),
    path('',home),
    path('register/',register),
    path('panel/',panel),
    path('services/',services),
    path('about/',about),
    path('contactus/',contactus) ,
    path('adminhome/',adminhome),
    path('searchEmployee/',searchEmployee)
]