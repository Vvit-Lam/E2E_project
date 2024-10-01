
from django.contrib import admin
from django.urls import include,path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from authentication import views #HodViews, StaffViews, StudentViews
from django.contrib.auth.decorators import login_required
from evav import settings
from django.conf.urls.static import static



urlpatterns = [
     #path('',views.auth,name='auth'),
    
     path('', views.home_page, name='home_page'),
     path('signin/',views.signin,name="signin"),
     path('signup/',views.signup,name='signup'),
     path('forgetpass/',views.forgetpass,name='forgetpass'),
     path('profile/', views.profile, name='profile'),
     path('logout/', views.logout_view, name='logout'),
     path('admino/', views.admino, name='admino'),
     path('faculty/', views.employee, name='faculty'),
     path('get_years/', views.get_years, name='get_years'),
     path('get_department/', views.get_departments, name='get_department'),
     path('get_sections/', views.get_sections, name='get_sections'),
     path('get_subjects/', views.get_subjects, name='get_subjects'),
     path('signup_staff/',views.signup_staff,name="signup_staff"),
     path('student/', views.student, name='student'),
     path('signup_admin/',views.signup_admin,name="signup_admin"),
     path('signup_student/',views.signup_student,name="signup_student"),
     path('do_admin_signup/',views.do_admin_signup,name="do_admin_signup"),
     path('do_staff_signup/',views.do_staff_signup,name="do_staff_signup"),
     path('insert_student/',views.insert_student_data, name='insert_student'),
     path('attendance_entry/', views.attendance_entry, name='attendance_entry'),
     path('attendance_updation/', views.attendance_updation, name='attendance_updation'),
     path('send_alert_email/', views.send_alert_email, name='send_alert_email'),
     path('success/', views.success, name='success'),
     path('email_success/', views.email_success, name='email_success'),
     path('profile/', views.profile, name='profile'),
     path('faculty-leave/', views.leave_request_view, name='faculty-leave'),
     path('student_leave_form/',views.permission_request_view,name='student_leave_form'),
     path('student_permission/',views.student_permission,name='student_permission'),
     path('student-leave/', views.student_leave, name='student-leave'),
     path('timetable/',views.timetable,name='timetable'),
     path('send-reset-email/', views.send_password_reset_email, name='send_reset_email'),
     path('success/', views.success, name='email_success'),
    # path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
     path('reset_password/', auth_views.PasswordResetView.as_view(template_name="authentication/reset_password.html"), name="reset_password"),
     path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="authentication/reset_password_sent.html"), name="password_reset_done"),
     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="authentication/reset_password_confirm.html"), name="password_reset_confirm"),
     path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="authentication/reset_password_complete.html"), name="password_reset_complete"),
     path('forgot_password/', views.send_password_reset_email, name='forgot_password'),
     path('resend_password_reset/', views.resend_password_reset_email, name='resend_password_reset_email'),

     #path('login_page/', views.login_page, name='login_page'), 
     
     
     


]#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




