from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date
from django.db import models
from django.core.exceptions import ValidationError


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    email = models.EmailField(default=None, unique=True, max_length=255)
    phone_number = PhoneNumberField(default=None, unique=True, null=True)


DAYS_CHOICES = [
    (20, 20),
    (25, 25),
    (30, 30),
]


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    number_of_days = models.IntegerField(choices=DAYS_CHOICES, default=20)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    objects = models.Manager()

    def __str__(self):
        return '%s %s' % (self.title, self.number_of_days)


def validate_age(value):
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age >= 18:
        return age
    else:
        raise ValidationError("Enter correct age.")


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(choices=GENDER_CHOICES, default=None, blank=True, max_length=2, null=True)
    date_of_birth = models.DateField(validators=[validate_age], default=None, blank=True, null=True)
    aadhar_card = models.FileField(upload_to='aadhar/', default=None, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile/', default='profile/profile.jpg', blank=True, null=True)
    address = models.TextField(default=None, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Course_enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    TIME_CHOICES = [
        ('Morning batch (7:30 to 11:00)', 'Morning batch (7:30 to 11:00)'),
        ('Afternoon batch (1:30 to 4:00)', 'Afternoon batch (1:30 to 4:00)'),
        ('Evening batch (5:30 to 8:00)', 'Evening batch (5:30 to 8:00)'),
    ]
    time_preference = models.CharField(max_length=30, choices=TIME_CHOICES, default=None, blank=False, null=False)

    def __str__(self):
        return '%s | %s | %s' % (self.student, self.course, self.time_preference)


class Schedule(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    student = models.OneToOneField(Course_enrollment, on_delete=models.CASCADE)
    TIMING_CHOICES = [
        ('7:30 a.m','7:30 a.m'),
        ('8:00 a.m', '8:00 a.m'),
        ('8:30 a.m', '8:30 a.m'),
        ('9:00 a.m', '9:00 a.m'),
        ('9:30 a.m', '9:30 a.m'),
        ('10:00 a.m', '10:00 a.m'),
        ('10:30 a.m', '10:30 a.m'),
        ('11:00 a.m', '11:00 a.m'),
        ('1:30 p.m', '1:30 p.m'),
        ('2:00 p.m', '2:00 p.m'),
        ('2:30 p.m', '2:30 p.m'),
        ('3:00 p.m', '3:00 p.m'),
        ('3:30 p.m', '3:30 p.m'),
        ('4:00 p.m', '4:00 p.m'),
        ('5:30 p.m', '5:30 p.m'),
        ('6:00 p.m', '6:00 p.m'),
        ('6:30 p.m', '6:30 p.m'),
        ('7:30 p.m', '7:30 p.m'),
        ('8:00 p.m', '8:00 p.m'),
    ]
    time_allocated = models.CharField(choices=TIMING_CHOICES, max_length=30, default=None)
    def __str__(self):
        return '%s | %s | %s' % (self.student, self.instructor, self.time_allocated)

class Attendance(models.Model):
    instructor = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    ATTENDANCE_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
    ]
    attendance_status = models.CharField(choices=ATTENDANCE_CHOICES, max_length=10, default=None)

    def __str__(self):
        return '%s | %s | %s' %(self.student, self.date, self.attendance_status)

class Report(models.Model):
    student_detail = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    STATUS_CHOICES =[
        ('Completed', 'Completed'),
        ('In Progress', 'In Progress'),
        ('Not started', 'Not started'),
    ]
    course_status = models.CharField(choices=STATUS_CHOICES, max_length=12, default='Not started')

    def __str__(self):
        return '%s | %s' %(self.student, self.course_status)


class Book_trial(models.Model):
    name = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=250, unique=True)
    phone_number = PhoneNumberField(default=None, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return '% s | %s' %(self.name, self.course)