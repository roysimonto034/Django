from django.db import models

# Create your models here.

class Employee(models.Model):
    emproll=models.IntegerField()
    empname = models.CharField(max_length=60)
    empdob = models.DateField()
    empmail= models.EmailField()
    phonenum = models.IntegerField(11)
    empaddr = models.TextField()