# Generated by Django 5.2.4 on 2025-07-15 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='teacher_id',
            new_name='teacher',
        ),
    ]
