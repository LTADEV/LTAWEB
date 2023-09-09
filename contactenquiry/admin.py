from django.contrib import admin

from contactenquiry.models import contactEnquiry
class Contactadmin(admin.ModelAdmin):
    list_display=('name','phone','email','message')
    
admin.site.register(contactEnquiry,Contactadmin)  

# Register your models here.
