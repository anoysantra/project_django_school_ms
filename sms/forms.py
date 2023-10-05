# smslog/forms.py
from django import forms
from .models import SMSLog

class SMSLogForm(forms.ModelForm):
    class Meta:
        model = SMSLog
        fields = ['sms_id','sender', 'recipient', 'message']
