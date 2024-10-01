from django.http import JsonResponse
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model,authenticate
import pymysql
import logging
from .forms import FacultyLeaveForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from .models import Year, Department, Section, Subject
from .forms import PermissionRequestForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login,logout
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.contrib.auth.hashers import make_password,check_password
from .models import Userr,Staffs,Admin,Student
from authentication.EmailBackend import EmailBackEnd
from django.conf import settings
from datetime import time, timedelta
import pytz
from .forms import FacultyLeaveForm
from .models import Faculty, ClassHour,Student
#from .models import UserProfile
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta, time
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from .models import Department, Year, Section, Subject



@login_required
def profile(request):
    user_profile = request.user.profile
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'authentication/profile.html', context)

def logout_view(request):
    logout(request)
    return redirect('signin')

def home_page(request):
    return render(request, 'authentication\index.html', {'title': 'Your Title Here'})


def validate_password(password):
    if len(password) < 9:
        raise ValidationError('Password must be at least 8 characters long.')

    if not any(char.isupper() for char in password):
        raise ValidationError('Password must contain at least one uppercase letter.')



def signup(request):
    if request.method == 'POST':
        username = request.POST.get('userName')
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')
        phone_number = request.POST.get('phonenumber')
        password = request.POST.get('password')
        confirm_password = request.POST.get('cpassword')
        try:
            user = Userr(email=email,userName=username,firstName=first_name,lastName=last_name,phonenumber=phone_number,password=make_password(password),cpassword=confirm_password)
            user.save()
            messages.success(request, 'Registration successful! Thank you.')
            return redirect('signin')
        except IntegrityError:
            # Handle the case when the username or email already exists
            messages.error(request, 'Username or email already exists.')
            return redirect('signup') 

    return render(request, "authentication/signup.html")

def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user_type = form.cleaned_data['user_type']
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                try:
                    if user.profile.user_type == user_type:  # Assuming user type is stored in a profile model
                        login(request, user)
                        if user_type == 'student':
                            return redirect('authentication/student.html')
                        elif user_type == 'teacher':
                            return redirect('authentication/faculty.html')
                        elif user_type == 'admin':
                            return redirect('authentication/admino.html')
                    else:
                        messages.error(request, 'Invalid user type')
                except AttributeError as e:
                    logging.error(f"AttributeError: {e}")
                    messages.error(request, 'User profile not found')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            logging.error("Form is not valid")
    else:
        form = LoginForm()
    
    return render(request, 'authentication/signin.html', {'form': form})
def signout(request):
    pass
def forgetpass(request):
     return render(request, 'authentication/reset_password.html')

def admino(request):
     return render(request, 'authentication/admino.html')
def employee(request):
     return render(request, 'authentication/faculty.html')
def student(request):
     return render(request, 'authentication/student.html')
def signup_admin(request):
    return render(request, 'authentication/signup_admin_page.html')
def signup_staff(request):
    return render(request, 'authentication/signup_staff_page.html')
def signup_student(request):
    return render(request, 'authentication/signup_student_page.html')


def do_admin_signup(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # Create and save new instance
            admin_signup = Admin (username=username, email=email,  password=make_password(password))
            admin_signup.save()
            messages.success(request, 'Signup successful.')
            return redirect('signin')  # Redirect to login page with success message
        except IntegrityError:
            # Handle the case when the username or email already exists
            messages.error(request, 'Username or email already exists.')
            return redirect('signup_admin')  # Redirect back to signup page with error message
    else:
        return render(request, 'authentication/signup_admin_page.html')

def do_staff_signup(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # Create and save new instance
            staff_signup = Staffs (username=username, email=email,  password=make_password(password))
            staff_signup.save()
            messages.success(request, 'Signup successful.')
            return redirect('signin')  # Redirect to login page with success message
        except IntegrityError:
            # Handle the case when the username or email already exists
            messages.error(request, 'Username or email already exists.')
            return redirect('signup_admin')

    else:
        return render(request, 'authentication/signup_staff_page.html')

def get_years(request):
    if request.method == 'GET':
        years = Year.objects.all()
        data = [{'id': year.id, 'name': year.name} for year in years]
        return JsonResponse(data, safe=False)

    
    
def get_departments(request):
    if request.method == 'GET':
        #year_id = request.GET.get('year_id')
        departments = Department.objects.all()
        data = [{'id': department.id, 'name': department.name} for department in departments]
        return JsonResponse(data, safe=False)


def get_sections(request):
    if request.method == 'GET':
        department_id = request.GET.get('department_id')
        sections = Section.objects.filter(department_id=department_id)
        data = [{'id': section.id, 'name': section.name} for section in sections]
        return JsonResponse(data, safe=False)

def get_subjects(request):
    if request.method == 'GET':
        year_id = request.GET.get('year_id')
        department_id = request.GET.get('department_id')
        subjects = Subject.objects.filter(year_id=year_id, department_id=department_id)
        data = [{'id': subject.id, 'name': subject.name} for subject in subjects]
        return JsonResponse(data, safe=False)
    
def attendance_entry(request):
    return render(request, 'authentication/student_attendance.html')
def attendance_updation(request):
    return render(request, 'authentication/updation.html')


def insert_student_data(request):
    if request.method == 'POST':
        student_name = request.POST.get('studentName')
        date_of_birth = request.POST.get('DOB')
        mobile_number = request.POST.get('mobileumber')
        email_id = request.POST.get('emailid')
        student_address = request.POST.get('studentaddress')
        join_date = request.POST.get('joindate')
        parent_mobile_number = request.POST.get('parent_mobile_number')

        # Create a new Student object and save it to the database
        student = Student(
            student_name=student_name,
            date_of_birth=date_of_birth,
            mobile_number=mobile_number,
            email_id=email_id,
            student_address=student_address,
            join_date=join_date,
            parent_mobile_number=parent_mobile_number 

        )
        student.save()

        # Redirect to a success page or another URL
        return redirect('profile')  # Replace 'success_url' with the actual URL name or path

    return render(request, 'authentication/newstudent.html')

def send_alert_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user_type = None
        
        if Userr.objects.filter(email=email).exists():
            user_type = 'Userr'
        elif Staffs.objects.filter(email=email).exists():
            user_type = 'Staff'
        elif Admin.objects.filter(email=email).exists():
            user_type = 'Admin'
        else:
            # If email doesn't exist in any table, render an error template
            return render(request, 'authentication/success.html', {'error': 'Email not found in any records.'})
            
        # Compose email content
        subject = 'Alert Message'
        if user_type in ['Admin', 'Staff']:
            message = 'Please verify attendance and class adjustments.'
        else:
            message = 'You have not been attending class regularly.'

        current_time_in_india = timezone.localtime(timezone.now(), pytz.timezone('Asia/Kolkata'))

        # Schedule the email to be sent at 9:00 AM in Indian Standard Time
        scheduled_time = current_time_in_india.replace(hour=9, minute=0, second=0, microsecond=0)
         
        if current_time_in_india.time() > time(hour=9):
            scheduled_time += timedelta(days=1)

        # Send email
        send_mail(subject, message, 'balaramakrishnatakkellapati75@gmail.com', [email], fail_silently=False)
        
        return redirect('email_success')  # Redirect to a success URL or view
    else:
        return render(request, 'authentication/sms.html')

def success(request):
    return render(request,'authentication/success.html')

'''def login_page(request):
    return render(request,'authentication/login_page.html')'''

def email_success(request):
    return render(request,'authentication/esuccess.html')

def profile(request):
    return render(request,"authentication/pro.html")

def leave_request_view(request):
    if request.method == 'POST':
        form = FacultyLeaveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Replace with your success URL
    else:
        form = FacultyLeaveForm()

    context = {
        'form': form,
        'faculties': Faculty.objects.all(),
        'class_hours': ClassHour.objects.all(),
    }
    return render(request, "authentication/faculty_leave_form.html", context)

def permission_request_view(request):
    if request.method == 'POST':
        form = PermissionRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Permission request submitted successfully!')
            return redirect('student_permission')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PermissionRequestForm()
    return render(request, 'authentication/student_leaveform.html', {'form': form})

def student_permission(request):
    return render(request,'authentication/permission.html')
def student_leave(request):
    return render(request,"authentication/leave.html")
def timetable(request):
    return render(request,"authentication/timetable.html")

'''def send_password_reset_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = None
        
        # Check for the user in different models
        if Userr.objects.filter(email=email).exists():
            user = Userr.objects.get(email=email)
        elif Staffs.objects.filter(email=email).exists():
            user = Staffs.objects.get(email=email)
        elif Admin.objects.filter(email=email).exists():
            user = Admin.objects.get(email=email)
        else:
            # If email doesn't exist in any table, render an error message
            return render(request, 'authentication/success.html', {'error': 'Email not found in any records.'})
        
        # If a user is found, generate a password reset link
        if user:
            # Generate a token for password reset
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))

            # Compose the password reset link
            reset_link = request.build_absolute_uri(
                reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
            )
            
            # Compose email content
            subject = 'Reset Your Password'
            message = f'You have requested to reset your password. Click the link below to reset it:\n{reset_link}\nIf you did not request this, please ignore this email.'

            current_time_in_india = timezone.localtime(timezone.now(), pytz.timezone('Asia/Kolkata'))

            # Schedule the email to be sent at 9:00 AM in Indian Standard Time
            scheduled_time = current_time_in_india.replace(hour=9, minute=0, second=0, microsecond=0)
            
            if current_time_in_india.time() > time(hour=9):
                scheduled_time += timedelta(days=1)

            # Send the password reset email
            send_mail(subject, message, 'admin@example.com', [email], fail_silently=False)
            
            return redirect('email_success')  # Redirect to a success page after sending the email
    else:
        return render(request, 'authentication/forgot_password.html')'''

def send_password_reset_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = None
        
        # Check for the user in different models
        if Userr.objects.filter(email=email).exists():
            user = Userr.objects.get(email=email)
        elif Staffs.objects.filter(email=email).exists():
            user = Staffs.objects.get(email=email)
        elif Admin.objects.filter(email=email).exists():
            user = Admin.objects.get(email=email)
        else:
            # If email doesn't exist in any table, render an error message
            return render(request, 'authentication/forgot_password.html', {'error': 'Email not found in any records.'})
        
        # If a user is found, generate a password reset link
        if user:
            # Generate a token for password reset
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))

            # Compose the password reset link
            reset_link = request.build_absolute_uri(
                reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
            )
            
            # Compose email content
            subject = 'Reset Your Password'
            message = f'You have requested to reset your password. Click the link below to reset it:\n{reset_link}\nIf you did not request this, please ignore this email.'

            # Schedule the email to be sent at 9:00 AM in Indian Standard Time
            current_time_in_india = timezone.localtime(timezone.now(), pytz.timezone('Asia/Kolkata'))
            scheduled_time = current_time_in_india.replace(hour=9, minute=0, second=0, microsecond=0)
            
            if current_time_in_india.time() > time(hour=9):
                scheduled_time += timedelta(days=1)

            # Send the password reset email
            send_mail(subject, message, 'admin@example.com', [email], fail_silently=False)
            
            return render(request, 'authentication/success.html', {'email': email})  # Redirect to success page
    else:
        return render(request, 'authentication/forgot_password.html')



def resend_password_reset_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = None
        
        # Check for the user in different models (same logic as before)
        if Userr.objects.filter(email=email).exists():
            user = Userr.objects.get(email=email)
        elif Staffs.objects.filter(email=email).exists():
            user = Staffs.objects.get(email=email)
        elif Admin.objects.filter(email=email).exists():
            user = Admin.objects.get(email=email)
        else:
            # If email doesn't exist in any table, render an error message
            return render(request, 'authentication/forgot_password.html', {'error': 'Email not found in any records.'})
        
        # Resend the reset email logic
        if user:
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))

            reset_link = request.build_absolute_uri(
                reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
            )
            
            subject = 'Reset Your Password (Resend)'
            message = f'This is a resend of your password reset link:\n{reset_link}\nIf you did not request this, please ignore this email.'

            send_mail(subject, message, 'admin@example.com', [email], fail_silently=False)

            return render(request, 'authentication/success.html', {'email': email})  # Redirect again after resending
    else:
        return redirect('forgot_password')  # Redirect if the request is not POST



def success(request):
    return render(request, 'authentication/success.html')


