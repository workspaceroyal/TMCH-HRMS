# Generated by Django 4.2.7 on 2024-01-11 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_remove_staff_leave_date_staff_leave_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_leave',
            name='end_date',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='staff_leave',
            name='start_date',
            field=models.CharField(max_length=100),
        ),
    ]
