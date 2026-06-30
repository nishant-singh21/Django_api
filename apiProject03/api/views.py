from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import  StudentSerializer


# CRUD oprations using APIView

class StudentAPI(APIView):
    # Read ALL or singhle data 
      def get(self, request, pk=None):
            if pk:
                try:
                     student = Student.objects.get(id = pk)
                     serializer = StudentSerializer(student)
                     return Response(serializer.data, status = status.HTTP_200_OK)
                except Student.DoesNotExist:
                    return Response({'detail': 'Student does not exist'}, status = status.HTTP_404_NOTFOUND)

            else:
                #  Read all data 
                students = Student.objects.all()
                serializer = StudentSerializer(students , many = True)
                return Response(serializer.data, status = status.HTTP_200_OK)
            
    # create data(POST)
      def post(self, request):
           serializer = StudentSerializer(data=request.data)
           if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status = status.HTTP_201_CREATED)
           return Response(serializer.errors, status = status.HTTP_400_BADREQUEST)

    # update data(PUT)
      def put(self, request , pk):
           try:
               student = Student.objects.all(pk=pk)
           except  Student.DoesNotExist:
                return Response({ "error": "Student not found "},  status =status.HTTP_404  )
           
           serializer = StudentSerializer(student, partial = True )
            
           if serializer.is_valid():
               serializer.save()
               return Response(serializer.data , status = status.HTTP_200_OK)
           return Response(serializer.error, status=status.HTTP_404_BAD_NOTFOUNDREQUESt)

    #   delete data(DELETE)
      def delete(self , request ,pk):
          try:
                student = Student.objects.get(id = pk)
                student.delete()
          except Student.DoesNotExist:
               return Response({"error": "Student does not exist"}, status = status.HTTP_404_NOTFOUND)
  
         
      
           


