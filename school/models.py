from datetime import datetime
from email.policy import default  
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

class School(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, unique=True, editable=False)
    school_name  = models.CharField(max_length=225)
    school_address  = models.CharField(max_length=225)
    date_registration  =  models.DateField()
    date_expiration  = models.DateField()
    is_active = models.BooleanField(default=False,)
    user  = models.OneToOneField(User, on_delete=models.CASCADE, unique=True,default=None, null=True,blank=True)
    def __str__(self):
        return self.school_name
    
    
class Class(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, unique=True, editable=False)
    school =  models.ForeignKey(School, on_delete=models.CASCADE,null=True)
    class_name  = models.CharField(max_length=225)
    is_active = models.BooleanField(default=False)
    def __str__(self):
        return self.class_name


class Section(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, unique=True, editable=False)
    school =  models.ForeignKey(School, on_delete=models.CASCADE,null=True)
    grade = models.ForeignKey(Class, on_delete=models.CASCADE,)
    section_name = models.CharField(max_length=225)
    is_active = models.BooleanField(default=False)
    def __str__(self):
        return self.section_name
    
class Parent(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, unique=True, editable=False)
    school =  models.ForeignKey(School, on_delete=models.CASCADE,null=True)
    parent_name = models.CharField(max_length=225)
    profile_pic = models.FileField(upload_to='profiles/',null=True)
    parent_middle_name = models.CharField(max_length=225,null=True)
    parent_last_name = models.CharField(max_length=225,null=True)
    parent_number =models.IntegerField(null=True)
    father_name = models.CharField(max_length=225,default='')
    father_middle_name = models.CharField(max_length=225,null=True)
    father_last_name = models.CharField(max_length=225,null=True)
    father_dob = models.DateField(default=datetime.now,blank=True)
    father_mobile_number = models.IntegerField(null=True)
    father_occupation = models.CharField(max_length=225,default='')
    Address = models.CharField(max_length=225,null=True)
    email = models.CharField(max_length=225,null=True)
    qualification = models.CharField(max_length=225,null=True)  #drop down Graduate, +2, SLC, Masters, other
    annual_income = models.IntegerField(null=True)
    mother_name = models.CharField(max_length=225, null=True)
    mother_middle_name = models.CharField(max_length=225,null=True)
    mother_last_name = models.CharField(max_length=225,null=True)
    mother_dob = models.DateField(default=datetime.now,blank=True)
    mother_mobile_number = models.IntegerField(null=True)
    mother_occupation = models.CharField(max_length=255,null=True)  #drop down, teacher, house wife, preature, other
    mother_email = models.CharField(max_length=225,null=True)
    qualification = models.CharField(max_length=225,null=True) #drop Graduate, +2, SLC, Masters, other
    user  = models.OneToOneField(User, on_delete=models.CASCADE, unique=True,default=None, null=True,blank=True)
    is_active = models.BooleanField(default=False, blank=True)
    def __str__(self):
        return self.parent_name

class Student(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, unique=True, editable=False)
    school =  models.ForeignKey(School, on_delete=models.CASCADE,null=True)
    grade  = models.ForeignKey(Class, on_delete=models.CASCADE,)
    section  = models.ForeignKey(Section, on_delete=models.CASCADE,)
    profile_pic = models.FileField(upload_to='profiles/',null=True)
    registration_date = models.DateField(auto_now=True)
    medium_of_education = models.CharField(max_length=255,null=True) # reate models
    first_name = models.CharField(max_length=225,null=False)
    middle_name = models.CharField(max_length=225,null=True)
    last_name = models.CharField(max_length=225,null=True)
    student_dob = models.DateField(default=datetime.now)
    student_gender = models.CharField(max_length=255,choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], null=True) # drop down
    email = models.CharField(max_length=225,null=True)
    mobile_no = models.IntegerField(null=True)
    alternate_mobile_no = models.IntegerField(null=True)
    country = CountryField() # drop down
    state = models.CharField(max_length=225,null=True) # drop down
    city = models.CharField(max_length=225,null=True) # drop down
    zip = models.CharField(max_length=225,null=True) # drop down
    roll_no = models.IntegerField(null=True)
    previous_school_name = models.CharField(max_length=225,null=True)
    previous_school_Address = models.CharField(max_length=225, null=True)
    transfer_certificate = models.FileField(upload_to='files/')
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE,null=True)
    user  = models.OneToOneField(User, on_delete=models.CASCADE, unique=True,default=None, null=True,blank=True)
    is_active = models.BooleanField(default=False,blank=True)
    def __str__(self):
        return self.first_name

class StaffPosstion(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, unique=True, editable=False)
    school =  models.ForeignKey(School, on_delete=models.CASCADE,null=True)
    positionName = models.CharField(max_length=255)
    def __str__(self):
        return self.positionName


class Staff(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, unique=True, editable=False)
    school =  models.ForeignKey(School, on_delete=models.CASCADE,null=True)
    profile_pic = models.FileField(upload_to='profiles/',default='')
    staff_name = models.CharField(max_length=225)
    Address = models.CharField(max_length=225)
    postion = models.ForeignKey(StaffPosstion, on_delete=models.CASCADE)
    salary = models.IntegerField(null=True)
    contact_number = models.IntegerField(null=True)
    email_address = models.CharField(max_length=225, null=True)
    user  = models.OneToOneField(User, on_delete=models.CASCADE, unique=True,default=None, null=True,blank=True)
    is_active = models.BooleanField(default=False,blank=True)
    def __str__(self):
        return self.staff_name
