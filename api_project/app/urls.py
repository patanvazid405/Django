from django.urls import path
from .views import home,add_employee,get_employee,get_emp

urlpatterns = [
    path('',home),
    path('add_employee/',add_employee),
    path('get_emp/<int:__id>/',get_emp),
    path('get_employee/',get_employee),

]