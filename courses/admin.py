from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Course_enrollment)
admin.site.register(Schedule)
admin.site.register(Attendance)
admin.site.register(Report)