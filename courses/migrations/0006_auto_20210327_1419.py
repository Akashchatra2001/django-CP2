# Generated by Django 3.1.6 on 2021-03-27 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20210323_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_picture',
            field=models.ImageField(blank=True, default='profile/profile.png', null=True, upload_to='profile/'),
        ),
    ]
