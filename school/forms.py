from dataclasses import fields
from django import forms
from .models import *

class RegisterStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields  = '__all__'

        

class RegisterStaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields  = '__all__'
        

class RegisterParentsForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields  = '__all__'