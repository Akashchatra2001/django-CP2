# Generated by Django 3.1.6 on 2021-04-02 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_attendance'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Attendance',
        ),
    ]