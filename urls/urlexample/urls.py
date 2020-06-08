from django.urls import path
from . import views

urlpatterns = [
    #order of path is impt, first comes username and then article path
    path('profile/<int:username>/', views.profile),
    path('profile/<slug:article_value>/', views.article),
    #path('profile/<int:username>/,views.profile),
    path('profile/', views.profile)
]