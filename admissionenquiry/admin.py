from django.contrib import admin

from admissionenquiry.models import admissionEnquiry
class Admissionadmin(admin.ModelAdmin):
    list_display=('name','phone','email','standard','location','message')
    
admin.site.register(admissionEnquiry,Admissionadmin)  
# Register your models here.
