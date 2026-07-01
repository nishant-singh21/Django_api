# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Student
# from .serializers import  StudentSerializer

from rest_framework import generics , mixins
from .models import Student 
from .serializers import StudentSerializer


# CRUD oprb using GenericAPIView and Mixins
class StudentListCreateAPI(
    generics.GenericAPIView, 
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    #read all data
    def get(self, request,*args, **kwargs):
        return self.list(request, *args, **kwargs)

    # create data
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class StudentRetrieveUpdateDeleteAPI(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # Get  single data
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    #  PUT update data
    def post(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # delete data
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



# # CRUD oprations using APIView

# class StudentAPI(APIView):
#     # Read ALL or singhle data 
#       def get(self, request, pk=None):
#             if pk:
#                 try:
#                      student = Student.objects.get(id = pk)
#                      serializer = StudentSerializer(student)
#                      return Response(serializer.data, status = status.HTTP_200_OK)
#                 except Student.DoesNotExist:
#                     return Response({'detail': 'Student does not exist'}, status = status.HTTP_404_NOTFOUND)

#             else:
#                 #  Read all data 
#                 students = Student.objects.all()
#                 serializer = StudentSerializer(students , many = True)
#                 return Response(serializer.data, status = status.HTTP_200_OK)
            
#     # create data(POST)
#       def post(self, request):
#            serializer = StudentSerializer(data=request.data)
#            if serializer.is_valid():
#                serializer.save()
#                return Response(serializer.data, status = status.HTTP_201_CREATED)
#            return Response(serializer.errors, status = status.HTTP_400_BADREQUEST)

#     # update data(PUT)
#       def put(self, request , pk):
#            try:
#                student = Student.objects.all(pk=pk)
#            except  Student.DoesNotExist:
#                 return Response({ "error": "Student not found "},  status =status.HTTP_404  )
           
#            serializer = StudentSerializer(student, partial = True )
            
#            if serializer.is_valid():
#                serializer.save()
#                return Response(serializer.data , status = status.HTTP_200_OK)
#            return Response(serializer.error, status=status.HTTP_404_BAD_NOTFOUNDREQUESt)

#     #   delete data(DELETE)
#       def delete(self , request ,pk):
#           try:
#                 student = Student.objects.get(id = pk)
#                 student.delete()
#           except Student.DoesNotExist:
#                return Response({"error": "Student does not exist"}, status = status.HTTP_404_NOTFOUND)






         
      
           


