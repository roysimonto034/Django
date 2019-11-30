from django.urls import path,include
from . import views

urlpatterns = [
    path('first/',views.firstname,name='firstname'),
    path('fourfunc/',views.fourfunc,name='fourfunc'),
    path('secondname/',views.secondname,name='secondname'),
]