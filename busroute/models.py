
from django.db import models


class Route(models.Model):
    route_id=models.CharField(max_length=5, primary_key=True)
    route_name=models.CharField(max_length=20)
    bus_operator=models.CharField(max_length=20)
    driver_id=models.CharField(max_length=20, unique=True)
    driver_name=models.CharField(max_length=20)
    contact_no=models.BigIntegerField()

 
    def __str__(self):
        return self.driver_name