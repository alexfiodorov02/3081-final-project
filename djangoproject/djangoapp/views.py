from django.shortcuts import render
from django.db.models import Q
from .models import Employee, Customer
from django.urls import resolve

def employees(request):
    employees = Employee.objects.all()
    return render(request, 'employees.html', {'employees': employees})

def customers(request):
    customers = Customer.objects.all()
    return render(request, 'customers.html', {'customers': customers})

def search(request, model, fields, template_name):
    query = request.GET.get('q')
    if query:
        q_objects = Q()
        for field in fields:
            q_objects |= Q(**{f'{field}__icontains': query})
        results = model.objects.filter(q_objects)
    else:
        results = model.objects.all()
    return render(request, template_name, {template_name.split('.')[0]: results})

def search_customers(request):
    fields = ['first_name', 'last_name', 'phone_number', 'email', 'company']
    return search(request, Customer, fields, 'customers.html')

def search_employees(request):
    fields = ['first_name', 'last_name', 'phone_number', 'email', 'role']
    return search(request, Employee, fields, 'employees.html')