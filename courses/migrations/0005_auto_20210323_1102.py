# Generated by Django 3.1.6 on 2021-03-23 05:32

import courses.models
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20210321_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='aadhar_card',
            field=models.FileField(blank=True, default=None, null=True, upload_to='aadhar/'),
        ),
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(blank=True, default=None, null=True, validators=[courses.models.validate_age]),
        ),
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], default=None, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='profile_picture',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='profile/'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default=None, max_length=128, null=True, region=None, unique=True),
        ),
    ]
