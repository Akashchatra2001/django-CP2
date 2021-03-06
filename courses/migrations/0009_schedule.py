# Generated by Django 3.1.6 on 2021-03-31 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20210331_1934'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.instructor')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='courses.course_enrollment')),
            ],
        ),
    ]
