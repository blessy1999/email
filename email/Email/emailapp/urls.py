from . import views
from django.urls import path

urlpatterns = [


    path('sendemail/',views.sendemail,name="sendemail"),

]