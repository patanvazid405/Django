from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import Employees
from rest_framework.response import Response


# Create your views here.

def home(req):
    return render(req,"home.html")

@api_view(["POST"])
def add_employee(req):
    n = req.data.get("name")
    a = req.data.get("age")
    d = req.data.get("dept")
    c = req.data.get("city")

    Employees.objects.create(name=n,age=a,dept=d,city=c)

    return Response("emp details added..") 
    