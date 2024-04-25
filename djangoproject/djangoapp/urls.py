from django.urls import path
from . import views

app_name = 'djangoapp'

urlpatterns = [
    path('employees/', views.employees, name='employees'),
    path('customers/', views.customers, name='customers'),
    path('search/', views.search, name='search'),
]
