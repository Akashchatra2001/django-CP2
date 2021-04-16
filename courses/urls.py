from datetime import datetime

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views
from django.urls import path
from .views import *
from courses import views, forms
from .forms import MySetPasswordForm, MyPasswordResetForm

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('course/', views.courses, name='courses'),
    path('register/', views.student_view.as_view(), name='register'),
    path('edit_profile/', login_required(views.user_edit_view.as_view()), name='edit_profile'),
    path('login/', LoginView.as_view(template_name='courses/login.html',
                                     authentication_form=forms.BootstrapAuthenticationForm,
                                     extra_context={
                                         'title': 'Log in',
                                         'year': datetime.now().year,
                                     }
                                     ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('user/', views.userPage, name='user'),
    path('password/', views.change_password, name='change_password'),
    path('account/', views.studentSettings, name="account"),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='courses/password_reset.html',
                                                                 form_class=MyPasswordResetForm),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='courses/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='courses/password_reset_confirm.html',
                                                     form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete',
         auth_views.PasswordResetCompleteView.as_view(template_name='courses/password_reset_complete.html'),
         name='password_reset_complete'),
    path('course-enroll/', login_required(views.CourseEnrollView.as_view()), name='course-enroll'),
    path('payment/', views.payment, name='payment'),
    path('success/' , views.success , name='success'),
    path('schedule/', views.scheduleview, name='schedule'),
    path('mycourse/', views.mycourseview, name='mycourse'),
    path('myattendance/', views.myattendance, name='attendance'),
    path('book_trial/', views.book_trial_view.as_view(), name='book_trial'),
]
