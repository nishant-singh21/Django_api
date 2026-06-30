from django.urls import path
from .views import StudentAPI

urlpatterns = [
    path('students/',StudentAPI.as_view()),# for get (all) and Post 
    path('students/<int:pk>/',StudentAPI.as_view()),# for GET (single) , PUY, DELETE
]