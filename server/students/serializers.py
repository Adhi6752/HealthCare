from rest_framework import serializers
from .models import Student,Result

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields=('Id','Text',
                'File')
        
