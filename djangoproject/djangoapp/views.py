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

def search_customers(request):
    query = request.GET.get('q')
    if query:
        results = Customer.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(phone_number__icontains=query) | Q(email__icontains=query) | Q(company__icontains=query))
    else:
        results = Customer.objects.all()
    return render(request, 'customers.html', {'customers': results})

def search_employees(request):
    query = request.GET.get('q')
    if query:
        results = Employee.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(phone_number__icontains=query) | Q(email__icontains=query) | Q(role__icontains=query))
    else:
        results = Employee.objects.all()
    return render(request, 'employees.html', {'employees': results})