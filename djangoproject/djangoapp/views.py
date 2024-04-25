from django.shortcuts import render
from .models import Employee, Customer

def employees(request):
    employees = Employee.objects.all()
    return render(request, 'employees.html', {'employees': employees})

def customers(request):
    customers = Customer.objects.all()
    return render(request, 'customers.html', {'customers': customers})
