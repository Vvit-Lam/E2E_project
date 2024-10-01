from django import forms
from .models import FacultyLeave, Faculty, ClassHour
from .models import PermissionRequest
#from .models import Department, Year, Section, Subject, Attendance



class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    user_type = forms.ChoiceField(choices=[('student', 'Student'), ('teacher', 'Teacher'), ('admin', 'Admin')])





class FacultyLeaveForm(forms.ModelForm):
    class Meta:
        model = FacultyLeave
        fields = ['name', 'leave_type', 'class_hours', 'adjust_faculty']
        widgets = {
            'leave_type': forms.Select(choices=[
                ('sick', 'Sick Leave'),
                ('emergency', 'Emergency Leave'),
                ('vacation', 'Vacation Leave'),
                ('casual', 'Casual Leave'),
                ('maternity', 'Maternity Leave')
            ]),
            'class_hours': forms.SelectMultiple(),
            'adjust_faculty': forms.SelectMultiple(),
        }




class PermissionRequestForm(forms.ModelForm):
    class Meta:
        model = PermissionRequest
        fields = ['date', 'from_time', 'to_time', 'counsellor', 'reason']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'from_time': forms.TimeInput(attrs={'type': 'time'}),
            'to_time': forms.TimeInput(attrs={'type': 'time'}),
            'reason': forms.Textarea(attrs={'rows': 4}),
        }



