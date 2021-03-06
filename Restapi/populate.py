import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Restapi.settings')#frontend--> project name
import django
django.setup()

from restapp.models import *
from faker import Faker
from random import *
faker=Faker()
def populate(n):
    for i in range(n):
        feno = randint(1001,90009)
        fename = faker.name()
        fesal = randint(57000,100000)
        feaddr = faker.city()
        emp_record = Employee.objects.get_or_create(empno=feno,empname=fename,empsal=fesal,eaddr=feaddr)
populate(30)