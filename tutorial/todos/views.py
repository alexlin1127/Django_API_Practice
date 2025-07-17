'''
檔案: views.py
作者: Alex LIN
功能: 建立Teacher, Student的API接口，及對應的CRUD操作
'''

# third-party
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

#app
from .models import Teachers, Students
from .serializers import StudentSerializer, TeacherSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer

    @action(detail=True, methods=['get'], url_path='showStudent')
    def show_student(self, request, pk=None):
        teacher = self.get_object()
        students = teacher.students.all()  # 使用 related_name='students'
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)