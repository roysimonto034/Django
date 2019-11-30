from django.urls import path
from . import views
urlpatterns=[
    path('fromdb/',views.modelview)
]