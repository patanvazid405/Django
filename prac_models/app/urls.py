from django.urls import path
from .views import home,add_employee,get_employee,get_one_emp,update_emp,delete_emp


urlpatterns = [
    path('',home),
    path('add_employee/',add_employee),
    path('show_employee/',get_employee),
    path('one_emp<int:__id>/',get_one_emp),
    path('update_emp<int:__id>/',update_emp),
    path('delete_emp<int:__id>/',delete_emp)
]
