# Generated by Django 4.2.7 on 2024-01-11 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_staff_leave_end_time_staff_leave_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_leave',
            name='end_date',
            field=models.CharField(max_length=100, null=True),
        ),
    ]