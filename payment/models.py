from django.db import models




class Payment(models.Model):
    payment_id=models.CharField(max_length=5, primary_key=True)
    payment_name=models.CharField(max_length=10)
 
    def __str__(self):
        return self.payment_name
