from django.urls import path
from django.conf.urls  import *
from . import  views

urlpatterns = [
    path('',views.index, name='home'),
    path('contact/',views.contact,name='contact'),
    path('portfolio/',views.portfolio,name='portfolio'),
]