from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Employee

# def second_view(request):
#     template=loader.get_template('myfirst.html')
#     return HttpResponse(template.render())

def first_view(request):
    employees = Employee.objects.all().values()
    template=loader.get_template('all_employees.html')
    context = {
        'employees': employees,
    }
    return HttpResponse(template.render(context,request))

def details(request, id):
    employee = Employee.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'employees':employee,
    }
    return HttpResponse(template.render(context,request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

# def testing(request):
#     """When get the specific coloumn"""
#     data = Employee.objects.all().values_list('fname')
#     template = loader.get_template('template.html')
#     context = {
#         'myemployees' : data,
#     }
#     return HttpResponse(template.render(context, request))

# def testing(request):
#     """To get all values"""
#     data = Employee.objects.all().values()
#     template = loader.get_template('template.html')
#     context = {
#         'myemployees' : data,
#     }
#     return HttpResponse(template.render(context, request))

# def testing(request):
#     """To get specific row"""
#     data = Employee.objects.filter(fname='Amala').values()
#     template = loader.get_template('template.html')
#     context = {
#         'myemployees' : data,
#     }
#     return HttpResponse(template.render(context, request))

def testing(request):
    """To get specific row"""
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry'], 
    }
    return HttpResponse(template.render(context, request))