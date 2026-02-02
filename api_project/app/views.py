from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import Employees
from rest_framework.response import Response
from django.forms.models import model_to_dict


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

@api_view(["GET"])
def get_employee(req):
    emp = Employees.objects.all().values()
    
    dataProcessing = []
    for i in emp:
        dataProcessing.append(i)
        print(i)
    
    return Response ({"emp":dataProcessing})
    
@api_view(["GET"])
def get_emp(req,__id):
    emp = Employees.objects.get(id=__id)
    dataProcessing = []
    for i in emp:
        dataProcessing.append(i)
        print(i)
    
    return Response ({"emp":model_to_dict(dataProcessing)})
    