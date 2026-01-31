from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import Employees
# Create your views here.
def home(req):
    return HttpResponse("home view")

@api_view(["POST"])
def add_employee(req):
    n=req.data.get("name")
    a=req.data.get("age")
    e=req.data.get("email")
    d=req.data.get("dept")
    Employees.objects.create(name=n,age=a,email=e,dept=d)
    return HttpResponse("emp added")    