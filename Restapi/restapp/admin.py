from django.contrib import admin
from . models import *
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
      list_display = [
           'id','empno','empname','empsal','eaddr'
      ]
admin.site.register(Employee,EmployeeAdmin)
