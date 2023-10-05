from django.db import models
from department.models import Department
# Create your models here.

class Teacher(models.Model):
    teacher_id = models.CharField(max_length=10, primary_key=True)
    teacher_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    dep_id = models.CharField(max_length=10)
    dep_name=models.CharField(max_length=30)

    def __str__(self):
        return self.teacher_name