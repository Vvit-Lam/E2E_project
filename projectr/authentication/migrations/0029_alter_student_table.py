# Generated by Django 4.2.10 on 2024-06-19 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0028_course_remove_attendancereport_attendance_id_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='student',
            table='userr',
        ),
    ]
