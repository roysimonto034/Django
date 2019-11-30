from django.urls import path
from . import views
urlpatterns=[
    path('',views.statview),
    path('showimage/',views.present_view),

]