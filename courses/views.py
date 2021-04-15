from datetime import datetime
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from .forms import StudentForm, StudentprofileForm, EditProfileForm, courseenrollForm, BookTrialForm
from .models import *


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'courses/index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
        }
    )


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'courses/contact.html',
        {
            'title': 'Contact',
            'message': 'Your contact page.',
            'year': datetime.now().year,
        }
    )


def courses(request):
    course = Course.objects.all()
    return render(request, 'courses/course.html', {'courses': course})


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'courses/about.html',
        {
            'title': 'About',
            'message': 'Your application description page.',
            'year': datetime.now().year,
        }
    )


class student_view(CreateView):
    model = User
    form_class = StudentForm
    template_name = 'courses/register.html'

    def form_valid(self, form):
        user = form.save()
        user.save()
        user = form.cleaned_data.get('username')
        return redirect('login')


class user_edit_view(UpdateView):
    model = User
    form_class = EditProfileForm
    template_name = 'courses/edit_profile.html'

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        user = form.save()
        user.save()
        user = form.cleaned_data.get('username')
        return redirect('user')

@login_required(login_url='login')
def userPage(request):
    return render(request, 'courses/user.html')

@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'courses/change_password.html', {
        'form': form
    })

@login_required(login_url='login')
def studentSettings(request):
    student = request.user.student
    form = StudentprofileForm(instance=student)

    if request.method == 'POST':
        form = StudentprofileForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'courses/student_settings.html', context)


class CourseEnrollView(CreateView):
    model = Course_enrollment
    form_class = courseenrollForm
    template_name = 'courses/course_enroll.html'

    def form_valid(self, form):
        enroll = form.save(commit=False)
        enroll.student = Student.objects.get(user= self.request.user)
        enroll.save()
        return redirect('user')


@login_required(login_url='login')
def scheduleview(request):
    schedule = Schedule.objects.all()
    return render(request, 'courses/schedule.html', {'schedule': schedule})

@login_required(login_url='login')
def mycourseview(request):
    student = Student.objects.get(user =request.user)
    mycourse = Course_enrollment.objects.filter(student = student )
    report = Report.objects.filter(student=student)
    context = {
        'mycourse': mycourse,
        'report': report,
    }
    return render(request, 'courses/mycourse.html', context)

@login_required(login_url='login')
def myattendance(request):
    student = Student.objects.get(user=request.user)
    mycourse = Course_enrollment.objects.filter(student=student)
    myschedule = Schedule.objects.filter(student=mycourse)
    attendance = Attendance.objects.filter(student=student)
    attendancecount = Attendance.objects.filter(student=student).count()




    context = {
        'attendancecount' : attendancecount,
        'attendance': attendance,
    }

    return render(request, 'courses/myattendance.html', context)

class book_trial_view(CreateView):
    model = Book_trial
    form_class = BookTrialForm
    template_name = 'courses/book_trial.html'

    def form_valid(self, form):
        user = form.save()
        user.save()
        user = form.cleaned_data.get('name')
        return redirect('home')