from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from formsapi.forms import *
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.serializers import serialize
from django.views.generic import View
from . utils import is_json
import json
# Create your views here.
def index(request):
    return render(request,'formsapi/index.html')

def forms_new_api(request):
    form=FormName()
    if request.method=='POST':
        print("hey entered post")
        form=FormName(request.POST)
        if form.is_valid():
            print("Validation Sucees")
            print("Ename:"+form.cleaned_data['name'])
            print("Email:"+form.cleaned_data['email'])
            print("TEXT:"+form.cleaned_data['text'])
    return render(request,'formsapi/forms_new.html',{'form':form})


def itemform(request):
  form=UserName()
  if request.method=='POST':
      print("It is Post request")
      form=UserName(request.POST)
      if form.is_valid():
         form.save(commit=True)
         return HttpResponse('<h1>Congarts you have successfully saved data</h1>')
      if form.errors:
          jsp_data = json.dumps(form.errors)
          return HttpResponse(jsp_data, status=400)
  else:
      print("Form is invalid")
  return render(request,'formsapi/formsubmit.html',{'forms':form})


class Itemserialize(View):
      def get(self,request,*args,**kwargs):
          data=Item.objects.all()
          #data=json.dumps(data)
          jsdata=serialize('json',data)
          #data=json.loads(jsdata)
          #data1=json.dumps(data)
          return HttpResponse(jsdata,content_type='application/json')

"""
    @csrf_exempt
     def mymeth(request):
         ...
         return pass
     @method_decorator(csrf_exempt,name='dispatch')
     class Empl(View):

"""

@method_decorator(csrf_exempt,name='dispatch')
class Workerserialize(View):

      def get_emp_id(self,id):
          try:
             wrk=Worker.objects.get(id=id)
          except Worker.DoesNotExist:
              wrk=None
          return wrk

      def get(self,request,*args,**kwargs):
          data=Worker.objects.all()
          jdata=serialize('json',data)
          return HttpResponse(jdata,content_type='application/json')

      def post(self,request):
          data=request.body
          valid=is_json(data)
          #print(json.loads(data))
          if not valid:
              rep={'msg':'please  pass a valid json'}
              dmps=json.dumps(rep)
              return HttpResponse(dmps,content_type='application/json')
          wdata=json.loads(data)
          #wdata=request.post
          form=Workername(wdata)
          if form.is_valid():
              form.save(commit=True)
              js_data=json.dumps({'msg':'Message stored successfully'})
              return HttpResponse(js_data,content_type='application/json')
          if form.errors:
             jsp_data=json.dumps(form.errors)
             return HttpResponse(jsp_data,status=400)

@method_decorator(csrf_exempt,name='dispatch')
class Workercurd(View):
      def get_emp_id(self,id):
          try:
             wrk=Worker.objects.get(id=id)
          except Worker.DoesNotExist:
              wrk=None
          return wrk
      def put(self,request,id,*args,**kwargs):
          #import pdb;pdb.set_trace()
          work=self.get_emp_id(int(id))
          print(work)
          if not work:
              data={"msg":"Worker detials doesnot exist for %d"%(id)}
              return JsonResponse(data,status=404)
          data=request.body
          valid=is_json(data)
          if valid is None:
              data=json.dumps({"msg":"The data passed is not valid json"})
              return HttpResponse(data,content_type='application/json',status=400)
          val_data=json.loads(data)
          orig_data={
              'name':work.name,
              'datejoin':work.salary,
              'salary': work.salary
          }
          orig_data.update(val_data)
          form=Workername(orig_data,instance=work)
          if form.is_valid():
             form.save(commit=True) 
             msg_all={'msg':'Data updated successfully'}
             return JsonResponse(msg_all,status=200)
          if form.errors:
             return JsonResponse(form.errors,status=400)

      def delete(self,request,id,*args,**kwargs):
          wrk=self.get_emp_id(int(id))
          print(wrk)
          if wrk is None:
             json_data={'msg':'No such record available'}
             return HttpResponse(json.dumps(json_data))
          status,del_item=wrk.delete()
          if status ==1:
             stat={'msg1':'Data deleted successfully'}
             return JsonResponse(stat)

          jsdata={'mymsg':'Srry data was not deleted plz try again'}
          return HttpResponse(json.dumps(jsdata),content_type='application/json')





