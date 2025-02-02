# Generated by Django 4.2.10 on 2024-03-14 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_studentsignup_userr_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=8)),
            ],
            options={
                'db_table': 'student_signup',
            },
        ),
        migrations.DeleteModel(
            name='StudentSignup',
        ),
    ]
