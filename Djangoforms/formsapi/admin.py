from django.contrib import admin
from . models import *
# Register your models here.
class Itemadmin(admin.ModelAdmin):
      list_display = [
          'id','ItemName','ItemId','ItemMail'
      ]
class Workeradmin(admin.ModelAdmin):
    lsit_display = [
        'id','Name','datejoin','salary'
    ]
admin.site.register(Item,Itemadmin)
admin.site.register(Worker,Workeradmin)