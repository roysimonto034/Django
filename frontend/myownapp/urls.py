from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.myfisrtview,name='myfirstview'),
    path('myown/',views.mysecondview),
    path('employe/',views.jinjaview,name='jinjaview'),
    path('mywish/',views.wish,name='wish'),

]
