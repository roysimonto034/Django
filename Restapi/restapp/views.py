from django.shortcuts import get_object_or_404,render
import json
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.generic import View
from django.core.serializers import serialize
from restapp.mixin import My_httpresponse_mixins
from . models import *
from . forms import EmployeeForm,Empmodel
# Create your views here.
# ---------------------------------------------function based views
def restmethod(request):
    empdata={
        'empname':'Jason',
        'emproll':2035,
        'empsal':354576,
        'empaddr':'Ranchi'
    }
    return HttpResponse(json.dumps(empdata),content_type='application/json')

def restmethod2(request):
    empdata={ 'empname':'Jaswinder', 'emproll':3454,
    'empsal':454576, 'empaddr':'Delhi' } 
    return JsonResponse(empdata)

#  -----------------------------------------------class based views

class JsonViews(View):

       def get(self,request,*args,**kwargs):
           empdata = {
               'empname': 'Jason',
               'emproll': 2035,
               'empsal': 763545,
               'empaddr': 'Ranchi'
               }
           data=json.dumps(empdata)
           return HttpResponse(data,content_type='application/json')

class JsonCbv(View):

      def get(self,request,*args,**kwargs):
          data={'msg':'This is a get request'}
          return JsonResponse(data)
      def post(self,request,*args,**kwargs):
          data={'msg':'This is a post request'}
          return JsonResponse(data)
      def put(self,request,*args,**kwargs):
          data={'msg':'This is a put request'}
          return JsonResponse(data)
      def delete(self,request,*args,**kwargs):
          data={'msg':'This is a delete request'}
          return JsonResponse(data)

#----------------------mixins---------------------------

class Importmixin(My_httpresponse_mixins,View):

    def get(self, *args, **kwargs):
        empdata = {
            'empname': 'Raghav',
            'emproll':  6054,
            'empsal':   873545,
            'empaddr': 'Delhi'
        }
        return self.render_response(empdata) #self is used as we are using instance method 'render_response'

class Myportmixin(My_httpresponse_mixins,View):

     def get(self,*args,**kwargs):
         epdata={
              'Student': 'Aminesh',
              'Roll': 4453566,
              'Dept': 'CSE',
              'School': 'Delhi Public School'
         }
         return self.render_http_response(epdata)



class Employeeview(View):

      def get(self,request,*args,**kwargs):
          emp = Employee.objects.get(id=30)
          empdata= {
                     'eno': emp.empno,
                     'ename': emp.empname,
                     'esal':  emp.empsal,
                      'eaddr': emp.eaddr
                  }
          jsondata = json.dumps(empdata)
          return HttpResponse(jsondata,content_type='application/json')

class Empgradview(View):
      def get(self,request,id,*args,**kwargs):
          emp = Employee.objects.get(id=id)
          empdata= {
                     'eno': emp.empno,
                     'ename': emp.empname,
                     'esal':  emp.empsal,
                      'eaddr': emp.eaddr
                  }
          jsdata = json.dumps(empdata)
          return HttpResponse(jsdata,content_type='application/json')

class Empserialize(View): #used mixins

      def get(self,request):
          emp=Employee.objects.all()
          jsdata = serialize('json',emp)
          #return HttpResponse(jsdata,content_type='application/json')
          return self.render_http_response(jsdata)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
class Token(APIView):
    permission_classes = (IsAuthenticated,)
    #http http://127.0.0.1:8000/restapi/jwttoken/ "Authorization: Token a0ed7c3fcd681b7874d848addaaecfbd6904749e"
    def get(self,request):
        content={"message":"Go corona go"}
        return Response(content)


class Demo(View):

      def get(selfself,request):
          #import pdb;pdb.set_trace()
          data = Employee.objects.all()
          mydict={}
          for i in range(5):
              mydata = {'emp'+str(i): data[i].empno,
                        'name'+str(i) : data[i].empname,
                        'sal'+str(i) : data[i].empsal,
                        'addr'+str(i) : data[i].eaddr
                      }
              mydict.update({'data'+str(i):mydata})
          mdta = json.dumps(mydict)
          return HttpResponse(mdta,content_type='application/json')

def emp_form(request):
    empl = EmployeeForm()
    return render(request,"restapp/forms.html",context={"form":empl})

def emp_form_add(request):
    if request.method == 'POST':
       #import pdb;pdb.set_trace()
       form = EmployeeForm(request.POST)
       if form.is_valid():
          try:
            name = form.cleaned_data["empname"]
            email = form.cleaned_data["email"]
            Indian = form.cleaned_data["Indian"]
            message = form.cleaned_data["message"]
            context = {"name" : name,
                       "email" : email,
                       "Indian" : Indian,
                       "message" : message}
            #form.save(commit=True)
            #return HttpResponse("form saved successfully")
            return render(request,"restapp/response.html",context=context)
          except:
            pass
    else:
        form = EmployeeForm()
        return render(request,"restapp/forms.html",context={"form":form}) 
        """above statement is invoked first which displays form othrwise no form will be displayed ,try comment it once"""



"""
context={"form":form} here key is importtant for render to template
form.save is available only for model forms

site: https://www.geeksforgeeks.org/django-crud-create-retrieve-update-delete-function-based-views/

"""

def empmodelform(request):
    if request.method == 'POST':
        #import pdb;pdb.set_trace()
        form = Empmodel(request.POST)
        if form.is_valid():
           form.save(commit=True)
           emp = Employee.objects.all().order_by('id')
           #return HttpResponse("<h1>Data Saved successfully</h1>")
           #return render(request,"restapp/display.html",context={"emp_data":emp})
           return show(request)
    else:
        form = Empmodel()
        return render(request,"restapp/modelforms.html",context={"form":form})

def show(request):
    data = Employee.objects.all().order_by('id')
    return render(request,"restapp/display.html",context={"emp_data": data}) 

def Delete(request,id):
    #emp = Employee.objects.get(id=id)
    emp = get_object_or_404(Employee,id=id)
    form = Empmodel(request.POST or None ,instance=emp)
    if request.method == "POST":
        emp.delete()
        return show(request)
    return render(request,"restapp/deleteform.html",context={"form":form})

def UpdateEmp(request,id):
    emp = Employee.objects.get(id=id)
    #import pdb;pdb.set_trace()
    form = Empmodel(request.POST or None ,instance=emp) 
    if form.is_valid():
       form.save(commit=True)
       return show(request)
    return render(request,"restapp/updateform.html",context={"form":form})  

