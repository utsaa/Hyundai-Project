from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.utils import timezone


# Create your models here.
class Owner(models.Model):
  id= models.AutoField(primary_key=True)
  name=models.CharField(max_length=100)
  address=models.CharField(max_length=500)
  contactno=models.CharField(max_length=13,default='')
  email=models.EmailField()
  password=models.CharField(max_length=500)
  grantlevel=models.BooleanField(null=True)

  def __str__(self):
      return f"{self.name} granted {self.grantlevel}"

class Car(models.Model):
  id=models.AutoField(primary_key=True)
  owner=models.ForeignKey('Owner', on_delete=models.CASCADE)
  model=models.CharField(max_length=100)
  color=models.CharField(max_length=100)
  carNo=models.IntegerField()
  RegNo=models.IntegerField()
  fueltype=models.CharField(max_length=500, null=True)
  mileage=models.CharField(max_length=1000, null=True)
  EnginePower=models.CharField(max_length=1000,null=True)
  EngineType=models.CharField(max_length=1000, null=True)

  def __str__(self) -> str:
      return f"{self.owner.name} car {self.model, self.color}"

class loginDetail(models.Model):
  id=models.AutoField(primary_key=True)
  loginName=models.CharField(max_length=100)
  loginDateTime=models.DateTimeField(default=timezone.now)
  owner=models.ForeignKey('Owner', on_delete=models.CASCADE)

  def __str__(self) -> str:
      return f"{self.loginName} of {self.owner.name}"

class Appointment(models.Model):
  id=models.AutoField(primary_key=True)
  DateTime=models.DateTimeField(default=timezone.now)
  emp=models.ForeignKey('Employee',on_delete=models.CASCADE)
  status=models.CharField(max_length=100)

  def __str__(self) -> str:
      return f"{self. emp} it is {self.status}"

class Service(models.Model):
  id=models.AutoField(primary_key=True)
  servname=models.CharField(max_length=100)
  servtype=models.CharField(max_length=100)
  fees=models.CharField(max_length=100)
  start_date=models.DateField(auto_now_add=True)
  end_date=models.DateField(blank=True, null=True)

  def __str__(self) -> str:
      return f"{self.servname} and type is {self.servtype}"



class CarService(models.Model):
  App=models.ForeignKey('Appointment',on_delete=models.CASCADE)
  Service=models.ForeignKey('Service', on_delete=models.CASCADE)

  def __str__(self) -> str:
      return f"application:{self.App.id} Service: {self.Service}"

class CarAppointment(models.Model):
  App=models.ForeignKey('Appointment',on_delete=models.CASCADE)
  Car=models.ForeignKey('Car', on_delete=models.CASCADE)

  def __str__(self) -> str:
      return f"application: {self.App.id} Car: {self.Car.id}"

class Employee(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    contact=models.CharField(max_length=13)

    def __str__(self) -> str:
        return f"{self.name} contact:{self.contact}"
