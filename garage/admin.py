from django.contrib import admin
from .models import Owner, Car, Appointment,loginDetail,Service, CarAppointment, CarService, Employee
# Register your models here.

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    class Meta:
        model=Owner
        fields='__all__'

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    class Meta:
        model=Car
        fields='__all__'

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    class Meta:
        model=Appointment
        fields='__all__'

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    class Meta:
        model=Service
        fields='__all__'

@admin.register(loginDetail)
class loginDetailAdmin(admin.ModelAdmin):
    class Meta:
        model=loginDetail
        fields='__all__'


@admin.register(CarAppointment)
class CarAppointmentAdmin(admin.ModelAdmin):
    class Meta:
        model=CarAppointment
        fields='__all__'

@admin.register(CarService)
class CarServiceAdmin(admin.ModelAdmin):
    class Meta:
        model=CarService
        fields='__all__'

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    class Meta:
        model=Employee
        fields='__all__'





