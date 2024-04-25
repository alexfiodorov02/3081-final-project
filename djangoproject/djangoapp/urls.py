from django.urls import path
from . import views

app_name = 'djangoapp'

urlpatterns = [
    path('', views.customers, name='customers'),
    path('employees/', views.employees, name='employees'),
    path('customers/', views.customers, name='customers'),
    path('search_customers/', views.search_customers, name='search_customers'),
    path('search_employees/', views.search_employees, name='search_employees'),
]
