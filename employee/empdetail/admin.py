from django.contrib import admin
from  .models import Employee
# Register your models here.
#jiva/Jiva@123
class EmpAdmin(admin.ModelAdmin):
    list_display = [
             'id','empname','emproll','empdob','empmail','phonenum','empaddr'
    ]
admin.site.register(Employee,EmpAdmin)
