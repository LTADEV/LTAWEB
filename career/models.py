from django.db import models
class Career(models.Model):
    FullTime='FT'
    PartTime='PT'
    car_type= [
        (FullTime, 'Full Time'),
        (PartTime, 'Part Time')
    ]
    career_title= models.CharField(max_length=50)
    career_exp=models.CharField(max_length=50)
    career_type=models.CharField(max_length=40, choices=car_type, default=FullTime)
    career_position=models.CharField(max_length=50)
    career_location=models.CharField(max_length=50)
    
# Create your models here.
