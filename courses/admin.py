from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Course_enrollment)
admin.site.register(Report)
admin.site.register(Book_trial)

class AttendanceInline(admin.StackedInline):
    model = Attendance

class ScheduleAdmin(admin.ModelAdmin):
    inlines = [AttendanceInline]

admin.site.register(Schedule,ScheduleAdmin)
admin.site.register(Attendance)
