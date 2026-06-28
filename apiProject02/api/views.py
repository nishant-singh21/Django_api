from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators  import api_view
from .models import Student 
from .serializers import  StudentSerializer
from rest_framework import status

@api_view(['GET'])
def get_student(request):
    students = Student.objects.all() # Get all students from database and store it in a variable called 'students' which is of type list. This will be used to serialize the data into JSON format.


    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def add_student(request):
    serializer =  StudentSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save() # Save the data to database.
        return Response(serializer.data, status = status.HTTP_201_CREATED )
    return Response(serializer.errors, status = status.HTTP_404_BAD_REQUEST)




