from django.shortcuts import render
from .models import Employee
# Create your views here.
def myfunc(request):
    emplist=Employee.objects.all()
    return render(request,'empdetail/index.html',context={'emply':emplist})
