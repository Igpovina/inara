from datetime import datetime
from pyexpat import model
from django.db import models

STATION_CHOICES = [
    ('CORIOLIS', 'Coriolis'),
    ('ORBITAL', 'Orbital'),
    ('REFINERY', 'Refinery'),
    ('PLANETARY', 'Planetary'),
]
SHIP_MAKE_CHOICES = [
    ('Zorgon Peterson','Zorgon Peterson'),
    ('DELANCY','DeLacy'),
    ('Saud Kruger', 'Saud Kruger'),
    ('LAKON', 'Lakon Spaceways'),
    ('GUTAMAYA', 'Gutamaya'),
    ('Core Dynamics','Core Dynamics'),
       
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
    img = models.ImageField(null=True, blank=True, upload_to="images/")
    location = models.ForeignKey(Station, on_delete = models.CASCADE)
    
    def __str__(self):
        return f'{self.model}'
    
    
class Commander(models.Model):
    name = models.CharField(max_length = 30)
    pub_date = models.DateField(blank = True)
    fleet = models.ForeignKey(Ships, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'CMDR {self.name}'
