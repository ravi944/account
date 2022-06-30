
from django.contrib import admin
from django.urls import path
from Account_App import views

urlpatterns = [
    path('get_details/',views.get_details),
    path('first_date/',views.first_date),
    path('last_date/',views.last_date),
    path('acc_num/',views.acc_num),
    path('ifsc_code/',views.ifsc_code),
]