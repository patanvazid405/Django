from django.db import models


# Create your models here.

class Employees(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    dept = models.CharField(max_length=20)
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.name


