# Generated by Django 4.2 on 2023-10-14 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_job_detail_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='info_employee',
            options={'verbose_name_plural': 'Info_Employee'},
        ),
        migrations.AlterModelOptions(
            name='job_catogery',
            options={'verbose_name_plural': 'job_catogery'},
        ),
        migrations.AlterModelOptions(
            name='job_detail',
            options={'verbose_name_plural': 'Job_Detail'},
        ),
    ]