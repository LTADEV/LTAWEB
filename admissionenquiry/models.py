from django.db import models

class admissionEnquiry(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    standard=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    message= models.TextField(null=True)
# Create your models here.
