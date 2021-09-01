from trash_collector import customers
from django.http import HttpResponseRedirect, HttpResponse
from django.urls.base import reverse
from .models import Employee
from django.http import request
from django.shortcuts import render
from django.apps import apps

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # This line will get the Customer model from the other app, it can now be used to query the db for Customers
    user = request.user
    logged_in_employee = Employee.objects.get(user=user)
    Customer = apps.get_model('customers.Customer')
    customers_in_employees_zip = Customer.objects.filter(zip_code=logged_in_employee.zip_code)
    for customers in logged_in_employee:

    
    
    
    context = {
        "customers": customers_in_employees_zip
    }
    return render(request, 'employees/index.html', context)

def create(request):

    if request.method == "POST":
        user = request.user
        name = request.POST.get('name')
        zip_code = request.POST.get('zip_code')
        new_employee = Employee(user = user, name = name, zip_code=zip_code)
        new_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/create.html')