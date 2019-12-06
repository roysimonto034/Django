from django.db import models
#'''admin/Jiva@123'''

# Create your models here.
class Employee(models.Model):
      empno = models.IntegerField()
      empname = models.CharField(max_length=60)
      empsal = models.IntegerField()
      eaddr = models.TextField()

