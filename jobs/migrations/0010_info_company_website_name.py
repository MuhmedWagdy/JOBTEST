# Generated by Django 4.2 on 2023-10-14 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_job_detail_product_catogery_alter_job_detail_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='info_company',
            name='website_name',
            field=models.URLField(blank=True, null=True),
        ),
    ]
