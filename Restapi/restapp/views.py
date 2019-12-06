from django.shortcuts import render
import json
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.generic import View
from django.core.serializers import serialize
from restapp.mixin import My_httpresponse_mixins
from . models import *

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
    empdata={
        'empname':'Jaswinder',
        'emproll':3454,
        'empsal':454576,
        'empaddr':'Delhi'
    }
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
         return self.render_http_reponse(epdata)



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




