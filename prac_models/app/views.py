from django.shortcuts import render
from django.http import HttpResponse
from .models import Employees
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.forms.models import model_to_dict


# Create your views here.
def home(req):
    return HttpResponse("home page")

@api_view(["POST"])
def add_employee(req):
    n = req.data.get("name")
    a = req.data.get("age")
    g = req.data.get("gender")

    Employees.objects.create(name = n,age=a,gender = g)

    return HttpResponse("add employee")

#Getting all data from the model(SQLLite) using GET from backend to frontend.. 
@api_view(["GET"])
def get_employee(req):
    emp = Employees.objects.all().values()
    return Response({"Employees":emp})

#getting an single person values using change to dict
@api_view(["GET"])
def get_one_emp(req,__id):
    emp = Employees.objects.get(id=__id)
    return Response ({"employees":model_to_dict(emp)})

#to update the existing data in DB
@api_view(["PUT"])
def update_emp(req,__id):
    n = req.data.get("name")
    a = req.data.get("age")
    g = req.data.get("gender")

    e = Employees.objects.get(id=__id)
    e.name = n
    e.age = a
    e.gender  = g
    e.save()
    return Response(f"emp-id{__id} got updated...") 

@api_view(["DELETE"])
def delete_emp(req,__id):
    e =Employees.objects.get(id=__id)
    e.delete()
    return HttpResponse(f"emp-id{__id} got DELETED...")