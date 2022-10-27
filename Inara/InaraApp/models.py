from datetime import datetime
from pyexpat import model
from django.db import models

STATION_CHOICES = [
    ('CORIOLIS', 'Coriolis'),
    ('ORBITAL', 'Orbital'),
    ('REFINERY', 'Refinery'),
]
# Create your models here.
class Station(models.Model):
    name = models.CharField(max_length = 30)
    type = models.CharField(max_length = 30, choices=STATION_CHOICES)
    system = models.CharField(max_length = 30)
    
    def __str__(self):
        return f'{self.name}'
    
class Ships(models.Model):
    make = models.CharField(max_length = 20)
    model = models.CharField(max_length = 20)
    img = models.ImageField(upload_to = "ships/")
    location = models.ForeignKey(Station, on_delete = models.CASCADE)
    
    
class Commander(models.Model):
    name = models.CharField(max_length = 30)
    img = models.ImageField(upload_to = "cmdr/")
    pub_date = models.DateField()
    fleet = models.ForeignKey(Ships, on_delete=models.CASCADE)
