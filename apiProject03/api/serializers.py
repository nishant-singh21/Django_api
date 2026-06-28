from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Mets:
        model = Student
        feild =  '__all__'

