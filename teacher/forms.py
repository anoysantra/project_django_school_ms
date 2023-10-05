from .models import Teacher
from django import forms


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['teacher_id', 'teacher_name', 'email', 'contact_number', 'address', 'dep_id','dep_name']