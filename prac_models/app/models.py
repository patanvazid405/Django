from django.db import models


# Create your models here.

class Employees(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=3)

def __str__(self):
    return self.name
