from django.shortcuts import render
from django.http import HttpResponse
import datetime
import os
# Create your views here.

def statview(request):
    return HttpResponse('<h1>hello Friends Whatsapp</h1>')

def present_view(request):
    date = datetime.datetime.now()
    hp=int(date.strftime('%H'))
    msg = "Hello: "+ os.environ.get('USERNAME')
    if hp<12:
        msg=msg+" Good Morning"
    elif hp<16:
        msg = msg+"Good Afternoon"
    else:
        msg = msg+" Good Evevning"
    return render(request,"staticapp/results.html",context = {'mymsg':msg})