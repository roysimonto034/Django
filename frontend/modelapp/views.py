from django.shortcuts import render
from modelapp.models import Employee
# Create your views here.
def modelview(request):
    employs=Employee.objects.all()
    return render(request,'modelapp/models.html',context={'emplys':employs})