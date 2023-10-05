from django.db import models


class Dormitory(models.Model):
    dormitory_id=models.CharField(max_length=5, primary_key=True)
    dormitory_name=models.CharField(max_length=10)
 
    def __str__(self):
        return self.dormitory_name
