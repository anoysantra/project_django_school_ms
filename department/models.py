from django.db import models


class Department(models.Model):
    dep_id=models.CharField(max_length=5, primary_key=True)
    dep_name=models.CharField(max_length=10)
 
    def __str__(self):
        return self.dep_name
