from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model= Payment
        fields=['payment_id','payment_name']