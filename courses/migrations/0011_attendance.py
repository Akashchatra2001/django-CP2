# Generated by Django 3.1.6 on 2021-04-02 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_schedule_time_allocated'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('attendance_status', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], default=None, max_length=10)),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.schedule')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.student')),
            ],
        ),
    ]
