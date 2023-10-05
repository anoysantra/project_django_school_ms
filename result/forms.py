from django import forms

from students.models import Student
from .models import MarkingStudents
from classes.models import Classes, Section

class MarkingStudentsForm(forms.ModelForm):
    class Meta:
        model = MarkingStudents
        fields = ['student_name', 'class_name', 'section_name', 'exam_type', 'marks_obtained']

"""
class StudentSearchMarksForm(forms.Form):
    class_name=forms.CharField(max_length=10, label='Enter Class to Search')
    section_name=forms.CharField(max_length=10,label='Enter Section to Search')
    student_name=forms.CharField(max_length=10,label='Enter Name to Search')
"""
class StudentSearchMarksForm(forms.Form):
    class_name = forms.ModelChoiceField(queryset=Classes.objects.all(), label='Enter Class to Search')
    section_name = forms.ModelChoiceField(queryset=Section.objects.all(), label='Enter Section to Search')
    student_name = forms.ModelChoiceField(queryset=Student.objects.all(), label='Enter Name to Search')
