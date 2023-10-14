from django.db import models
from django.contrib.auth.models import User
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

Category_type = (

    ('Creative Agency','Creative Agency'),  
    ('Programming','Programming'),
    ('Sales Erp','Sales Erp'), 
    ('Pos Hardware','Pos Hardware'),

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
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    job_name = models.CharField(max_length=100,choices=name_jobs)
    catogory_job = models.ForeignKey(job_catogery, on_delete=models.CASCADE)
    place = models.CharField(max_length=200)
    def Check_Salary(salary):
        if salary not in range(3500,4000):        
           raise ValidationError("Salary Must Between in range(3500-4000)")
        
        else:
            return(" must Choose correct salary")
        

    salary = models.FloatField(max_length=10,validators=[Check_Salary])
    product_catogery = models.CharField(max_length=100,choices=Category_type)
    time_puplish = models.DateTimeField(null=True,blank=True)
    def __str__(self) -> str:
        return str(self.user)




class Info_Company(models.Model):
    class Meta:
        verbose_name_plural = 'Info_Company' 
    name = models.EmailField(max_length=200)
    logo = models.ImageField(upload_to='ImageLogo',height_field=None, width_field=None, max_length=None)
    mobile =models.CharField( max_length=50)
    website_name = models.URLField(null=True,blank=True)
    comany_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name





    
















