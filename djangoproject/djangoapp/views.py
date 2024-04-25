from django.shortcuts import render
from django.db.models import Q
from .models import Employee, Customer

def employees(request):
    employees = Employee.objects.all()
    return render(request, 'employees.html', {'employees': employees})

def customers(request):
    customers = Customer.objects.all()
    return render(request, 'customers.html', {'customers': customers})

def search(request):
    query = request.GET.get('q')
    if query:
        current_page = resolve(request.path_info).url_name

        if current_page == 'customers':
            results = Customer.objects.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(phone_number__icontains=query) |
                Q(email__icontains=query) |
                Q(company__icontains=query)
            )
        elif current_page == 'employees':
            results = Employee.objects.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(phone_number__icontains=query) |
                Q(email__icontains=query) |
                Q(role__icontains=query)
            )
    else:
        if current_page == 'customers':
            results = Customer.objects.all()
        elif current_page == 'employees':
            results = Employee.objects.all()

    return render(request, f'{current_page}.html', {current_page: results})