from django.urls import path
from . import views

urlpatterns=[
    path('restdata/',views.restmethod),
    path('restval/',views.restmethod2),
    path('classbased/',views.JsonViews.as_view()),
    path('curdview/',views.JsonCbv.as_view()),
    path('mixin/',views.Importmixin.as_view()),
    path('httpmixin/',views.Myportmixin.as_view()),
    path('emprest/',views.Employeeview.as_view()),
    path('api/(?P<id>\d+)/$',views.Empgradview.as_view()),
    path('apiview/',views.Empserialize.as_view()),
]