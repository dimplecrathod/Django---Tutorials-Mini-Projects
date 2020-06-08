from django.urls import path
from . import views

urlpatterns =[
    path('', views.index),
    path('car/', views.car),
    path('car_class', views.CarView.as_view()),
]