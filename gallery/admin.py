from django.contrib import admin
from gallery.models import Gallery
class Galleryadmin(admin.ModelAdmin):
    list_display=('gallery_title','gallery_tag','gallery_image')
    
admin.site.register(Gallery,Galleryadmin)    
# Register your models here.
