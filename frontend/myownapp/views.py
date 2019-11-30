from django.shortcuts import render
from django.http import  HttpResponse
import datetime

def myfisrtview(request):
    return HttpResponse('<h1> Hello Django todays date is:'+str(datetime.datetime.now())+'</h1>')

def mysecondview(request):
    return HttpResponse('<h1> Hello fuckers todays date is:'+str(datetime.datetime.now())+'</h1>')

def jinjaview(request):
    dta=datetime.datetime.now()
    myinfo=['Simo',30,1500000]
    return render(request,'myownapp/index.html',context={'nm':myinfo[0],'ag':myinfo[1],'sal':myinfo[2],'dtes':dta})

def wish(request):
    date=datetime.datetime.now()
    h=int(date.strftime('%H'))
    msg='Hello Guys|||Very Good'
    if h<12:
        msg=msg+' Morning'
    elif h<16:
        msg=msg+' Afternoon'
    else:
        msg=msg+' Evening'
    return render(request,'myownapp/wishlist.html',context={'msg':msg})
