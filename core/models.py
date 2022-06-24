from email import message
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    
    def __str__(self) -> str:
        return self.name



class UserService(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return f"{self.client} -> {self.service} | {'aktywny' if self.active else 'nieaktywny'}"
    

class PaymentMethods(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name


class Payments(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    method = models.ForeignKey(PaymentMethods, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    to_pay = models.IntegerField()
    payed = models.IntegerField(default=0)
    realized = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f"{self.date} | {self.client} zapłacił {self.payed} PLN"

class Messages(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employee')
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='client')
    message = models.TimeField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField()
    
    
class Statistics(models.Model):
    total_subsribers = models.BigIntegerField()
    total_clients = models.BigIntegerField()
    current_workout = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.date
    
class Visits(models.Model):
    entrace = models.DateTimeField(auto_now_add=True)
    exited = models.DateTimeField(blank=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.CharField(max_length=50)
    visits = models.IntegerField(default=0)
