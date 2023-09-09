from django.contrib import admin
from career.models import Career
class Careeradmin(admin.ModelAdmin):
    list_display=('career_title','career_exp','career_type','career_position','career_location')
    
admin.site.register(Career,Careeradmin)    
# Register your models here.
