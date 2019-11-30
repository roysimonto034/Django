from django.urls import path,include
from . import views
urlpatterns=[
    path('tblview/',views.tableview,name='tableview'),
]