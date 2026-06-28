from django.urls import path 
from .import  views


urlpatterns = [
    path('students/', views.get_student ,  name='get_student'),
    path('students/add', views.add_student , name ='add_student'),
]