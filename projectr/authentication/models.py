
from django.db import models
import datetime

# Get the current year
current_year = datetime.datetime.now().year

print(f"The current year is {current_year}")


# models.py


class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    student_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=10)
    email_id = models.EmailField(max_length=254)
    student_address = models.CharField(max_length=200)
    join_date = models.DateField()
    date_of_birth = models.DateField()
    parent_mobile_number = models.CharField(max_length=10)
    #user_type = models.CharField(max_length=10, default='student')
    class Meta:
        managed = False
        db_table = 'student'


class Userr(models.Model):
    email = models.EmailField(max_length=254, primary_key=True)
    userName = models.CharField(max_length=255)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=15)
    password = models.CharField(max_length=12)
    cpassword = models.CharField(max_length=8)
    #user_type = models.CharField(max_length=255,default='student')

    class Meta:
        managed = False
        db_table = 'userr'

class Year(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'year'

class Department(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    year = models.ForeignKey(Year, on_delete=models.CASCADE, related_name='departments')
    class Meta:
        managed = False
        db_table = 'department'

class Section(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'section'

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'subject' 



class Staffs(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=150)
    class Meta:
        managed = False
        db_table = 'authentication_staffs'

class NotificationStudent(models.Model):
    #id = models.AutoField(primary_key=True)
    email = models.EmailField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'notification_student'
   
class NotificationStaff(models.Model):
    #id = models.AutoField()
    email = models.EmailField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'notification_staff'
    
    
    

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    #usertype = models.CharField(max_length=50, default='admin')
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=150)
    
    class Meta:
        managed = False
        db_table = 'admin_signup'
    
    
class Faculty(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ClassHour(models.Model):
    time_slot = models.CharField(max_length=50)

    def __str__(self):
        return self.time_slot


class FacultyLeave(models.Model):
    name = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=50, choices=[
        ('sick', 'Sick Leave'),
        ('casual', 'Casual Leave'),
        ('earned', 'Earned Leave'),
        ('maternity', 'Maternity Leave'),
        ('paternity', 'Paternity Leave')
    ])
    class_hours = models.ManyToManyField(ClassHour)
    adjust_faculty = models.ManyToManyField(Faculty, related_name='adjusted_faculty')

    def __str__(self):
        return f"{self.name} - {self.leave_type}"

    class Meta:
        db_table = 'faculty_leave_details'

class Counsellor(models.Model):
    name = models.CharField(max_length=100)
    email= models.EmailField(max_length=255,null=True)

    def __str__(self):
        return self.name

class PermissionRequest(models.Model):
    date = models.DateField()
    from_time = models.TimeField()
    to_time = models.TimeField()
    counsellor = models.ForeignKey(Counsellor, on_delete=models.CASCADE)
    reason = models.TextField()

    def __str__(self):
        return f"Permission from {self.from_time} to {self.to_time} on {self.date}"