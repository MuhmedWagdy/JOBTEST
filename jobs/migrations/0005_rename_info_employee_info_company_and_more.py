# Generated by Django 4.2 on 2023-10-14 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_alter_info_employee_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Info_employee',
            new_name='Info_Company',
        ),
        migrations.AlterModelOptions(
            name='info_company',
            options={'verbose_name_plural': 'Info_Company'},
        ),
    ]