from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone

from django.core.exceptions import ValidationError



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

    class Meta:
        verbose_name_plural = 'job_catogery' 

    job_type = models.CharField(max_length=200,choices=job_type)

    job_location = models.CharField(max_length=200)
    
    def non_negative_validator(experience):
        if experience <=0:
           raise ValidationError("Value must be Choose At least One Or More experience")

    experience = models.IntegerField(validators=[non_negative_validator])

    posted_within = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.job_type


class Job_Detail(models.Model):

    class Meta:
        verbose_name_plural = 'Job_Detail' 

    job_name = models.CharField(max_length=100,choices=name_jobs)
    catogory_job = models.ForeignKey(job_catogery, on_delete=models.CASCADE)
    place = models.CharField(max_length=200)
   

    def Check_Salary(salary):
        if salary  not in range(3500,4000):
           
           raise ValidationError("Salary Must Between in range(3500-4000) ")
    salary = models.FloatField(validators=[Check_Salary])


    time_puplish = models.DateTimeField(null=True,blank=True)

    def __str__(self) -> str:
        return self.job_name




class Info_Company(models.Model):
    class Meta:
        verbose_name_plural = 'Info_Company' 

    
    name = models.EmailField(max_length=200)
    logo = models.ImageField(upload_to='ImageLogo',height_field=None, width_field=None, max_length=None)
    mobile =models.CharField( max_length=50)
    comany_name = models.CharField(max_length=50)



    def __str__(self):
        return self.name





    
















