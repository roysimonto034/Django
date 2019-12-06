import requests
#from restapp.views import *

# base_url='http://localhost:8000'
# addon='/restapi/restdata/'
# response=requests.get(base_url+addon)
# opt=response.json()
# print(opt['empname']+' is from '+opt['empaddr'])

base_url1='http://localhost:8000'
addon1='/restapi/classbased/'
#response=requests.get(base_url1+addon1)
addon2='/restapi/curdview/'
response=requests.get(base_url1+addon2)
#print(response.json())
# -------------------------to execute these below csrf cookie has to be defined or disabled in middleware
response=requests.post(base_url1+addon2)
#print(response.json())
response=requests.put(base_url1+addon2)
#print(response.json())
response=requests.delete(base_url1+addon2)
#print(response.json())

#----------------------mixins
mixon='/restapi/mixin/'
response=requests.get(base_url1+mixon)
#print(response.json())

# ----------------curd operations using Class Based views
#
def mytest():
    #import requests
    base_url1 = 'http://localhost:8000'
    end_url = '/restapi/emprest/'
    response = requests.get(base_url1+end_url)
    print(response.status_code)
    print(response.json())
    print(type(response))
#mytest()

def mytest1():
    #import requests
    base_url3 = 'http://localhost:8000'
    end_url3 = '/restapi/api/'
    id = input("enter some id: ")
    response = requests.get(base_url3+end_url3+id+'/')
    print(response.status_code)
    #print(response.json())
    #print(type(response))
mytest1()