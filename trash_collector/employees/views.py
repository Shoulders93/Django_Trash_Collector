from django.http import HttpResponseRedirect, HttpResponse
from django.urls.base import reverse
from .models import Employee
from .models import Customers
from django.http import request
from django.shortcuts import render
from django.apps import apps
from django.utils import timezone

todays_date = models.DateField(default=timezone)
print(todays_date)


# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # This line will get the Customer model from the other app, it can now be used to query the db for Customers
    Customer = apps.get_model('customers.Customer')
    user = request.user
    logged_in_employee = Employee.objects.get(user=user)
    customers_in_employees_zip = Customers.objects.filter(zip_code=logged_in_employee.zip_code)
    customers_same_zip = []
    customers_pickup_today = []
    for customer in Customers:
        if customers_in_employees_zip == logged_in_employee.zip_code:
            customers_same_zip.append(customer)

    for customer in customers_same_zip:
        if customer.weekly_pickup_day == logged_in_employees_zip or customer.one_time_pickup == today:
            customers_pickup_today.append(customer)
    
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