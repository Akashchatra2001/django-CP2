# Generated by Django 3.1.6 on 2021-03-21 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20210314_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default=None, max_length=255, unique=True),
        ),
    ]