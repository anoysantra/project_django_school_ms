from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model= Student
        fields='__all__'

class StudentSearchForm(forms.Form):
    class_name=forms.CharField(max_length=10, label='Enter Class to Search')
    section_name=forms.CharField(max_length=10,label='Enter Section to Search')
