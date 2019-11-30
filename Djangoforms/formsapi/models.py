from django.db import models


class Item(models.Model):
      ItemName = models.CharField(max_length=60)
      ItemId = models.IntegerField()
      ItemMail = models.EmailField()
# Create your models here.

class Worker(models.Model):
      name=models.CharField(max_length=60)
      datejoin=models.DateField()
      salary=models.IntegerField()


