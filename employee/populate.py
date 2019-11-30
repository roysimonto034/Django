import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','employee.settings')#frontend--> project name
import django
django.setup()
import random
from faker import Faker
from empdetail.models import *
def phonenum():
    sum=random.randint(8,9)
    ps=''+str(sum)
    for i in range(9):
       ps=ps+str(random.randint(1,9))
    return ps

def populate(val):
    for i in range(val):
        fake=Faker()
        enm=fake.name()
        erl=fake.random_int(min=1,max=999)
        phn=phonenum()
        edob=fake.date()
        email=fake.email()
        eadr=fake.address()
        emprec=Employee.objects.get_or_create(empname=enm,emproll=erl,phonenum=phn,empdob=edob,empmail=email,empaddr=eadr)

populate(10)

