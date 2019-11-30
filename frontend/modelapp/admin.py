from django.contrib import admin
from .models import Employee
# Register your models here.
class Employeeadmin(admin.ModelAdmin):
    list_display=[
        'id','empno','empname','empsal','eaddr']
admin.site.register(Employee,Employeeadmin)
