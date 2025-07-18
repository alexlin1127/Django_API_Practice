'''
檔案: models.py
作者: Alex LIN
功能: 建立DB模型(Table) --> python 物件
物件: Teachers, Students
'''

from django.db import models

class Teachers(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Students(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    grade = models.IntegerField()
    enrolled_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='student_images/', blank=True, null=True)


    teacher = models.ForeignKey(
        Teachers,
        on_delete=models.CASCADE,
        related_name='students',
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name
    
