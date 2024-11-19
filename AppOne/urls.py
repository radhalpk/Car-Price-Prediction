from django.urls import path
from AppOne.views import *

app_name='AppOne'

urlpatterns=[
    path('base/',base,name='base_view'),
]