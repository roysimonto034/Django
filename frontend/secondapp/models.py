from django.db import models

'''user/pass= admin/Jiva@123'''
# Create your models here.
class Employee(models.Model):
    empno = models.IntegerField()
    empname = models.CharField(max_length=64)
    empsal = models.IntegerField()
    eaddr = models.CharField(max_length=64)

    def __str__(self):
        return self.empname

