from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("fname","lname","joined_date",)
admin.site.register(Employee,EmployeeAdmin)
