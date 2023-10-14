from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

job_type = (
    ('Full Time','Full Time'),  
    ('Part Time','Part Time'),
    ('Remote','Remote'), 
    ('Freelance','Freelance'),

)

name_jobs = (
    ('python devoloper','python devoloper'),  
    ('Digtal Marketer','Digtal Marketer'),
    ('Database Administrator','Database Administrator'), 
    ('Odoo Devoloper','Odoo devoloper'),



)

class job_catogery(models.Model):

    job_type = models.CharField(max_length=200,choices=job_type)

    job_location = models.CharField(max_length=200)

    experience = models.IntegerField()

    posted_within = models.DateTimeField(default=timezone)



class Job_Detail(models.Model):

    logo = models.ImageField(upload_to="image_logo")

    job_name = models.CharField(max_length=100,choices=name_jobs)

    catogory_job = models.ForeignKey(job_catogery, on_delete=models.CASCADE)

    place = models.CharField(max_length=200)

    salary = models.FloatField(range(3500,4000))

    time_puplish = models.DateTimeField(null=True,blank=True)
















