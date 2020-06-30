from django.db import models

# Create your models here.

class Port(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    dec = models.TextField()
    capacity = models.IntegerField()
    offer = models.BooleanField(default=False)
    annualtraffic = models.IntegerField()
    datetraffic = models.DateField()
    #introYear = models.CharField(max_length=4)
    #containers = models.IntegerField()
    #mobileBodies = models.IntegerField()
    #unaccompaniedTrailers = models.IntegerField()
