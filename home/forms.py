from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'name',
            'age',
            'address',
        ]

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','id':'name_input'}),
            'age':forms.NumberInput(attrs={'class':'form-control','id':'age_input'}),
            'address':forms.TextInput(attrs={'class':'form-control','id':'address_input'}),
        }