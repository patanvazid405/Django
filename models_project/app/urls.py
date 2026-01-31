
from django.urls import path
from .views import home,add_employee
urlpatterns=[
    path("",home) ,
    path("add_employee/",add_employee) 
]