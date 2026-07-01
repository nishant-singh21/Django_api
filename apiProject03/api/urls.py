# from django.urls import path
# from .views import StudentAPI

# urlpatterns = [
#     path('students/',StudentAPI.as_view()),# for get (all) and Post 
#     path('students/<int:pk>/',StudentAPI.as_view()),# for GET (single) , PUY, DELETE

# ]


from django.urls import path
from .views import StudentListCreateAPI, StudentRetrieveUpdateDeleteAPI

urlpatterns = [
    path('students/', StudentListCreateAPI.as_view()),
    path('students/<int:pk>/', StudentRetrieveUpdateDeleteAPI.as_view()),
]