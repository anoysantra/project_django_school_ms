from django import forms
from .models import Library

class LibraryForm(forms.ModelForm):
    class Meta:
        model= Library
        fields=['book_id','title','author','quantity','isbn']