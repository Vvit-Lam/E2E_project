# Generated by Django 4.2.10 on 2024-03-19 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0023_alter_staff_signup_password_alter_userr_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='parent_mobile_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
