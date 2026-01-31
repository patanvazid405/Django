from django.db import models


# Create your models here.
class Employees(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.CharField(max_length=20)
    dept = models.CharField(max_length=10)

def __str__(self):
    return self.name

