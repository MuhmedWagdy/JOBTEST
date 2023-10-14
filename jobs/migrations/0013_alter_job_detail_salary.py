# Generated by Django 4.2 on 2023-10-14 19:01

from django.db import migrations, models
import jobs.models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0012_alter_job_detail_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_detail',
            name='salary',
            field=models.FloatField(max_length=10, validators=[jobs.models.Job_Detail.Check_Salary]),
        ),
    ]