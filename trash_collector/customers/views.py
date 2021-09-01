from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render
from .models import Customer
from django.urls import reverse


# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user
    context = {}
    try:
        # This line inside the 'try' will return the customer record of the logged-in user if one exists
        logged_in_customer = Customer.objects.get(user=user)
        context["logged_in_customer"] = logged_in_customer
    except:
        # TODO: Redirect the user to a 'create' function to finish the registration process if no customer record found
        pass

    # It will be necessary while creating a Customer/Employee to assign request.user as the user foreign key

    print(user)
    return render(request, 'customers/index.html', context)


def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        user = request.user
        address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        weekly_pickup_day = request.POST.get('weekly_pickup_day')
        new_customer = Customer(name=name, user=user, address=address, zip_code=zip_code, weekly_pickup_day=weekly_pickup_day)
        new_customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/create.html')

def edit(request):
    # changed user = user to user = logged_in_customer
    user = request.user
    logged_in_customer = Customer.objects.get(user=user)
    
    if request.method == "POST":
        logged_in_customer.name = request.POST.get('name')
        logged_in_customer.address = request.POST.get('address')
        logged_in_customer.zip_code = request.POST.get('zip_code')
        logged_in_customer.weekly_pickup_day = request.POST.get('weekly_pickup_day')
        logged_in_customer.one_time_pickup = request.POST.get('one_time_pickup')
        logged_in_customer.suspend_start = request.POST.get('suspend_start')
        logged_in_customer.suspend_end = request.POST.get('suspend_end')
        logged_in_customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        context = {
            "logged_in_customer": logged_in_customer
        }
        return render(request, "customers/update.html", context)