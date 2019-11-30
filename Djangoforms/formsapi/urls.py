from django.urls import path,re_path
from . import views
urlpatterns=[
    path('api/',views.index,name='index'),
    path('form_api/',views.forms_new_api,name='forms_new_api'),
    path('form_submit/',views.itemform,name='itemform'),
    path('form_sub/',views.Itemserialize.as_view()),
    path('post_request/',views.Workerserialize.as_view()),
    re_path(r'^put_del_request/(?P<id>\d+)/$',views.Workercurd.as_view()),
    ]