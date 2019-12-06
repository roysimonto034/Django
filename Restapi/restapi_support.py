-----------------------------------------------------------------------------views.py------------from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from mynewapp.mixin import *
import json
from . models import *

# Create your views here.
def mymethod(request):
 return HttpResponse('<h1>hello Django we are here</h1>')

def rendermethod(request):
 return render(request,'mynewapp/index.html',context={'name':'Wiprorites'})


class EmployeeCSV(View):
	 def get(self,request,ids=151):
		try:
			empdata=Employee.objects.get(id=ids)
	    except Employee.DoesNotExist:
			mydata={'error':'No data found'}
			#jsondata = json.dumps(mydata)
			#return HttpResponse(jsondata, content_type='application/json',status=404)
			return JsonResponse(mydata,status=404)
		else:
			jsondata = serialize('json', [empdata, ])
			return HttpResponse(jsondata,content_type='application/json',status=200)
			#jsondata=serialize('json',[empdata,],fields=['empid','empname'])


class EmployeeBld(Employeemixin,View):
	def get(self,request):
		data=Employee.objects.all()
		return self.gernerate_reponse(data)

class SelectedView(Employeemixin,View):
     def get(self,request):
         epdata=Employee.objects.all()
         return self.modiresponse(epdata)
		 
-------------mixin.pyimport json
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from mynewapp.models import *


class Employeemixin(object):

 def gernerate_reponse(self, jsondata):
	jsdata = serialize('json', jsondata)
	return HttpResponse(jsdata,content_type='application/json')

 def modiresponse(self,jsondata):
	jsdata=serialize('json',jsondata)
	pdata=json.loads(jsdata)
	pflist=[]
	for eip in pdata:
		pflist.append(eip.get('fields'))
		jsond=json.dumps(pflist)
	return HttpResponse(jsond,content_type='application/json',status=200)

	---------------------------testapi.py

import requests

Base_url='http://localhost:8000'
endurl='/mynewproj/apiview/'
endurl2='/mynewproj/restapp/'

def show_all():
 resp= requests.get(Base_url+endurl)
 print(resp.status_code)
 print(resp.json())

def show_one():
 resp = requests.get(Base_url + endurl2)
 print(resp.status_code)
 print(resp.json())

show_one()
----------------------------urls.py

from django.urls import path
from . import views
urlpatterns = [
 path('finalapp/',views.mymethod,name='mymethod'),
 path('',views.rendermethod,name='rendermethod'),
 #path('restapp/(?P<id>\d+)/$',views.EmployeeCSV.as_view()),
 path('restapp/',views.EmployeeCSV.as_view()),
 path('api/',views.EmployeeBld.as_view()),
 path('apiview/',views.SelectedView.as_view()),
]