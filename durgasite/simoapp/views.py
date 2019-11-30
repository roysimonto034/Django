from django.shortcuts import render
from django.http import HttpResponse
import datetime
tim=datetime.datetime.now()
def firstname(request):
    return HttpResponse('<h1>Hello This is Zeta App: '+str(tim)+'Your time starts now </h1')

def secondname(request):
    return HttpResponse('<h1>Hello Pandu thi is second App:'+str(tim)+': '+str(request.content_type)+'Your 2nd method is </h1>')


# def third(func):
#     print('first '+func.__name__ +' will be executed first')
#     def inner(*args):
#         func()
#     inner()


def fourfunc(request):
    return HttpResponse('<h1> The Square of '+str(5)+' is: '+str(5**2))


# Create your views here.
