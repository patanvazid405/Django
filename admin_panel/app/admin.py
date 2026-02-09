from django.contrib import admin
from .models import Patients

# Register your models here.
@admin.register(Patients)
class PatientsAdmin(admin.ModelAdmin):
    list_display = ("name","age","city")
    list_display_links = ("name","city") # to edit the details
    list_filter = ("city",)
    list_editable = ()
    

