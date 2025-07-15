'''
檔案:serializer.py
作者: Alex LIN
功能: 將model建立的python物件轉換為json格式
物件: Teachers, Students
'''

# third-party module
from rest_framework import serializers

# self-define module
from .models import Teachers, Students


class TeacherSerializer(serializers.ModelSerializer):
    # name, subject設定為 not null，這邊做二次驗證。
    name = serializers.CharField(
        required = True,
        max_length = 50,
        min_length = 1,
        error_messages = {
            'required': '名稱為必填欄位',
            'max_length': '名稱不能超過50字元'
        }
    )

    subject = serializers.CharField(
        required = True,
        max_length = 32,
        min_length = 2,
        error_messages = {
            'required': '科目為必填欄位',
            'max_length': '內容不能超過32字元'
        }
    )
    class Meta:
        model = Teachers
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required = True,
        max_length = 50,
        min_length = 1,
        error_messages = {
            'required': '名稱為必填欄位',
            'max_length': '名稱不能超過50字元'
        }
    )

    grade = serializers.IntegerField(
        required = True,
        min_value = 1,
        max_value = 12,
        error_messages = {
            'required': '年級為必填欄位',
            'min_value': '年級不能小於1',
            'max_value': '年級不能大於12',
            'invalid': '請輸入有效的數字'
        }
    )

    teacher_name = serializers.CharField(source='teacher.name', read_only=True)

    class Meta:
        model = Students
        fields = '__all__'
        exclude = ['teacher']