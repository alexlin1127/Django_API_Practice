'''
檔案: views.py
作者: Alex LIN
功能: 建立Teacher, Student的API接口，及對應的CRUD操作
'''

# origin
import os
import mimetypes
from django.http import FileResponse, Http404

# third-party
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# app
from .models import Teachers, Students
from .serializers import StudentSerializer, TeacherSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

    @action(detail=True, methods=['get'], url_path='image')
    def get_image(self, request, pk=None):
        student = self.get_object()
        
        # 檢查學生是否有上傳圖片
        if student.image:
            # 取得實際檔案路徑
            image_path = student.image.path
            
            if os.path.exists(image_path):
                content_type, _ = mimetypes.guess_type(image_path)

                if not content_type or not content_type.startswith('image/'):
                    content_type = 'image/jpeg'

                return FileResponse(open(image_path, 'rb'), content_type=content_type)
        
        raise Http404("圖片不存在")

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer

    @action(detail=True, methods=['get'], url_path='showStudent')
    def show_student(self, request, pk=None):
        teacher = self.get_object()
        students = teacher.students.all()  # 使用 related_name='students'
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)