from django import forms
from .models import Dormitory

class DormitoryForm(forms.ModelForm):
    class Meta:
        model= Dormitory
        fields=['dormitory_id','dormitory_name']