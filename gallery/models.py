from django.db import models
class Gallery(models.Model):
    Campus='campus'
    Transportation='transportation'
    Infrastructure = 'infra'
    Lab = 'lab'
    Activity='activity'
    Events='event'
    
    gallery_type= [
        (Campus, 'Campus'),
        (Transportation, 'Transportation'),
        (Infrastructure, 'Infrastructure'),
        (Lab,'Lab'),
        (Activity, 'Activity'),
        (Events, 'Events')
    ]
    gallery_title= models.CharField(max_length=50)
    gallery_tag=models.CharField(max_length=50, choices=gallery_type,default=Campus)
    gallery_image= models.FileField(upload_to="gallery/",max_length=250, null=False, default=None)
# Create your models here.
