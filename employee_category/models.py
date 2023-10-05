from django.db import models

class Employee(models.Model):
    category_id=models.CharField(max_length=5, primary_key=True)
    category_name=models.CharField(max_length=50)

    def __str__(self):
        return self.category_name
