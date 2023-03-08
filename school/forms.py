from dataclasses import fields
from django import forms
from .models import *
from .functions import *

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
        
        

class RegisterClassesForm(forms.ModelForm):
    class Meta:
        model = Class
        fields  = '__all__'
        

class RegisterSectionsForm(forms.ModelForm):
    class Meta:
        model = Section
        fields  = '__all__'
