from django.contrib import admin


from .models import job_catogery,Job_Detail,Info_employee
# Register your models here.

admin.site.register(job_catogery)
admin.site.register(Job_Detail)
admin.site.register(Info_employee)

