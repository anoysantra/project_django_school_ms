from django.db import models

class SMSLog(models.Model):
    sms_id=models.CharField(max_length=10,primary_key=True)
    sender = models.CharField(max_length=255)
    recipient = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender