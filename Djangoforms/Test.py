import requests
import datetime
import json
from dateutil.tz import tzutc

def create_timestamp(obj):
    if isinstance(obj,(datetime.date,datetime.datetime)):
        return obj.isoformat()

def create_resource():
    base_url='http://localhost:8000'
    addon='/djangoforms/post_request/'
    mydata={
     'name':'Manohar',
     'datejoin':'2016-08-05',# very important
     'salary':6970898,
    }
    arrdata =  {'name':'Rahul',
                 'datejoin':'2017-04-02',
                  'salary':567568,
                 }
    arrdata1=  {'name':'Hemant',
                'datejoin':'2015-03-06',
                'salary':658678,
                   }
    arrdata2 =  {
                    'name':'Gajendra',
                    'datejoin':'2014-08-07',
                     'salary':37346,
                  }
    arrdata3={      'name':'Vishnu',
                    'datejoin':'2013-11-07',
                     'salary':693469
                }
    #for validation of salry
    #data_dumps=json.dumps(mydata,default=create_timestamp)
    data_dumps = json.dumps(arrdata3)
    resp=requests.post(base_url+addon,data=data_dumps)
    print(resp.status_code)
    print(resp.json())
#create_resource()

def update_resource(id):
    base_url='http://localhost:8000'
    addon='/djangoforms/put_del_request/'
    mydata= {'name':'Monty',
             'datejoin':'2013-07-08',
             'salary': 1390090}
    mdata={'name':'Abhinav',
           'datejoin':'2012-03-07',
            'salary':1090090
           }
    resp=requests.put(base_url+addon+str(id)+'/',data=json.dumps(mydata))
    print(resp.status_code)
    print(resp.json())
#update_resource(1)

def del_resource(id):
    base_url = 'http://localhost:8000'
    addon = '/djangoforms/put_del_request/'
    resp = requests.delete(base_url + addon + str(id) + '/')
    print(resp.status_code)
    print(resp.json())
del_resource(3)
'''
python manage.py dumpdata formsapi.Worker --indent 4

[
{
    "model": "formsapi.worker",
    "pk": 1,
    "fields": {
        "name": "Ashutosh",
        "datejoin": "2019-11-08",
        "salary": 565576
    }
},
{
    "model": "formsapi.worker",
    "pk": 2,
    "fields": {
        "name": "Prartik",
        "datejoin": "2019-06-05",
        "salary": 7354356
    }
},
{
    "model": "formsapi.worker",
    "pk": 3,
    "fields": {
        "name": "Manohar",
        "datejoin": "2016-08-05",
        "salary": 6970898
    }
},
{
    "model": "formsapi.worker",
    "pk": 4,
    "fields": {
        "name": "Rahul",
        "datejoin": "2017-04-02",
        "salary": 567568
    }
},
{
    "model": "formsapi.worker",
    "pk": 5,
    "fields": {
        "name": "Hemant",
        "datejoin": "2015-03-06",
        "salary": 658678
    }
},
{
    "model": "formsapi.worker",
    "pk": 6,
    "fields": {
        "name": "Indranil",
        "datejoin": "2016-09-08",
        "salary": 557346
    }
},
{
    "model": "formsapi.worker",
    "pk": 7,
    "fields": {
        "name": "Vishnu",
        "datejoin": "2013-11-07",
        "salary": 693469
    }
}
]
'''