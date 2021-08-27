from django.db import models

# Create your models here.

# TODO: Create an Employee model with properties required by the user stories


class Customer(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)\
    