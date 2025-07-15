'''
檔案:views.py
作者: Alex LIN
功能: 建立Teacher, Student的API接口，及對應的CRUD操作
'''

from rest_framework import viewsets
from .models import Teachers, Students
from .serializers import StudentSerializer, TeacherSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer
