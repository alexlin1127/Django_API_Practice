from rest_framework import viewsets
from .models import Teachers, Students
from .serializers import StudentSerializer, TeacherSerializer
# from rest_framework.response import Response

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer