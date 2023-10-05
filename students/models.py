from django.db import models


class Student(models.Model):
    student_id=models.CharField(max_length=5, primary_key=True)
    name=models.CharField(max_length=50)
    dob=models.DateField()
    address=models.CharField(max_length=50)
    contact_no=models.PositiveBigIntegerField()
    class_name=models.CharField(max_length=10)
    section_name=models.CharField(max_length=100)


    def __str__(self):
        return self.name
