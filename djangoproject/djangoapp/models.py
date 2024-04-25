from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator, EmailValidator, RegexValidator

class Employee(models.Model):
    first_name = models.CharField(max_length=255, validators=[MinLengthValidator(3), MaxLengthValidator(255)])
    last_name = models.CharField(max_length=255, validators=[MinLengthValidator(3), MaxLengthValidator(255)])
    phone_number = models.CharField(max_length=15, validators=[MinLengthValidator(10), MaxLengthValidator(15), RegexValidator(r'^\+?1?\d{9,15}$')])
    email = models.EmailField(max_length=255, validators=[MinLengthValidator(3), MaxLengthValidator(255), EmailValidator()])
    role = models.CharField(max_length=255, validators=[MinLengthValidator(3), MaxLengthValidator(255)])

class Customer(models.Model):
    first_name = models.CharField(max_length=255, validators=[MinLengthValidator(3), MaxLengthValidator(255)])
    last_name = models.CharField(max_length=255, validators=[MinLengthValidator(3), MaxLengthValidator(255)])
    phone_number = models.CharField(max_length=15, validators=[MinLengthValidator(10), MaxLengthValidator(15), RegexValidator(r'^\+?1?\d{9,15}$')])
    email = models.EmailField(max_length=255, validators=[MinLengthValidator(3), MaxLengthValidator(255), EmailValidator()])
    company = models.CharField(max_length=255, validators=[MinLengthValidator(3), MaxLengthValidator(255)])

