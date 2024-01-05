from django.urls import path
from . import views

urlpatterns = [
    path('', views.chart1, name='index'),
    path('town/', views.chart2, name='index2'),
    path('item_type/', views.chart3, name='index3'), 
]