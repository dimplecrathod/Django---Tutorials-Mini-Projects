from django.contrib import admin
from django.urls import path

from .views import index
from .views import ifchanged
from .views import prog

urlpatterns =[
    path('', index, name="index"),
    path('ifchanged', ifchanged, name="ifchanged" ),
    path('<programmer_id>/', prog, name="prog"),
]