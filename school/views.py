import json
import re
from unicodedata import name
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core import serializers
from .models import *
from .functions import*
from datetime import date
from .forms import *

def index(request):
    return render(request,'index.html', {'title': 'test'})

def login_user(request):
    messages = []
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username= username, password= password)
        if user:
            login(request,user)
            messages.append('Logged In')
            return redirect('/dashboard')
        else:
            messages.append('Cannot Login')
            
    return render(request,'login.html', {'title': 'Login Page', 'messages': messages})

def signup(request):
    messages = []
    return render(request,'signup.html', {'title': 'test', 'messages': messages})

def notfound(request):
    return render(request,'404.html', {'title': '404 - Not Found',})

@login_required(login_url='/login')
def dashboard(request):
    user = request.user
    context = {'title': 'test', 'school': '','dashboardData':{}}
    if user.is_authenticated:
        school = getschool(request)
        if school != None:
            d1 = school.date_expiration;
            context['school'] = school
            context['dashboardData']['students'] = len(getStudents(request))
            context['dashboardData']['staffs']  = len(getStaffs(request))
            context['dashboardData']['days_left']  = days_between(d1,  date.today())
            context['dashboardData']['classes'] = len(getClasses(request))
            context['dashboardData']['parents'] = len(getParents(request))
            return render(request,'dashboard.html',context)
        else:
            logout(request)
            return redirect('/404')
    else:
        return redirect('/login')

@login_required(login_url='/login')
def students(request):
    school = getschool(request)
    if not school:
        return redirect('/login')
    students = getStudents(request)
    classes = getClasses(request)
    context ={'school': school, 'students': students, 'classes': classes}
    return render(request, 'students.html', context)

@login_required(login_url='/login')
def staff(request):
    school = getschool(request)
    if not school:
        return redirect('/404')  
    staffs = getStaffs(request)
    positions = getPositions(request)
    context ={'school': school, 'staffs': staffs, 'positions': positions}
    return render(request, 'staff.html', context)

@login_required(login_url='/login')
def parents(request):
    school = getschool(request)
    if not school:
        return redirect('/404')
    parents = getParents(request)
    context ={'school': school, 'parents': parents}
    return render(request, 'parents.html', context)

@login_required(login_url='/login')
def register(request, type):
    pv_id_if_exist = request.GET.get('id')
    school = getschool(request)
    messages =  []
    if not school:
        return redirect('/404')
    form  = None
    if type == 'student':
        if pv_id_if_exist != None:
            obj = Student.objects.filter(id=pv_id_if_exist)
            if obj:
                form = RegisterStudentForm(instance=obj[0])
        else:
            form = RegisterStudentForm()
    elif type == 'staff':
        if pv_id_if_exist != None:
            obj = Staff.objects.filter(id=pv_id_if_exist)
            if obj:
                form = RegisterStaffForm(instance=obj[0])
        else:
            form = RegisterStaffForm()
 
    elif type == 'parents':
        if pv_id_if_exist != None:
            obj = Parent.objects.filter(id=pv_id_if_exist)
            if obj:
                form = RegisterParentsForm(instance=obj[0])
        else:
            form = RegisterParentsForm()
    if request.method == 'POST':
        if pv_id_if_exist == None:
            if type == 'student':
                form = RegisterStudentForm(request.POST,request.FILES)
            elif type == 'staff':
                form = RegisterStaffForm(request.POST,request.FILES)
            elif type == 'parents':
                form = RegisterParentsForm(request.POST,request.FILES)
        else:
            if type == 'student':
                obj = Student.objects.filter(id=pv_id_if_exist)
                form = RegisterStudentForm(request.POST,request.FILES, instance=obj[0])
            elif type == 'staff':
                obj = Staff.objects.filter(id=pv_id_if_exist)
                form = RegisterStaffForm(request.POST,request.FILES, instance=obj[0])
            elif type == 'parents':
                obj = Parent.objects.filter(id=pv_id_if_exist)
                form = RegisterParentsForm(request.POST,request.FILES, instance=obj[0])
        if form.is_valid():
            if pv_id_if_exist == None:
                form.save()
                messages.append('Added Successfully')
            else:
                form.save()
                if type == 'student':
                    if pv_id_if_exist != None:
                        obj = Student.objects.filter(id=pv_id_if_exist)
                        if obj:
                            form = RegisterStudentForm(instance=obj[0])
                    else:
                        form = RegisterStudentForm()
                elif type == 'staff':
                    if pv_id_if_exist != None:
                        obj = Staff.objects.filter(id=pv_id_if_exist)
                        if obj:
                            form = RegisterStaffForm(instance=obj[0])
                    else:
                        form = RegisterStaffForm()
            
                elif type == 'parents':
                    if pv_id_if_exist != None:
                        obj = Parent.objects.filter(id=pv_id_if_exist)
                        if obj:
                            form = RegisterParentsForm(instance=obj[0])
                    else:
                        form = RegisterParentsForm()
                messages.append('Updated Successfully')
            
        else:
            print('not valid')
        
    context = {'school': school, 'form': form, 'messages': messages}
    if type == 'student':
        context['classes'] = getClasses(request)
        context['sections'] = {}
    return render(request, 'register.html', context)

@login_required(login_url='/login')
def profile(request):
    school = getschool(request)
    if not school:
        return redirect('/404')
    context ={'school': school}
    return render(request, 'profile.html', context)

@login_required(login_url='/login')
def sections(request, grade):
    resp = [];
    data = getSections(request, grade)
    for d in data:
        resp.append({
            'name': d.section_name,
            'id': d.id
        })
    return JsonResponse(resp , safe=False)

@login_required(login_url='/login')
def gradeapi(request):
    resp = [];
    data = getClasses(request)
    for d in data:
        resp.append({
            'name': d.class_name,
            'id': d.id
        })
    return JsonResponse(resp , safe=False)

@login_required(login_url='/login')
def academics(request, type):
    context = {}
    return render(request, 'academics.html',context)

@login_required(login_url='/login')
def grades(request):
    school = getschool(request)
    grades = getClasses(request)
    context = {'classes': grades,'school': school}
    return render(request, 'classes.html',context)

@login_required(login_url='/login')
def sectionsquery(request,grade):
    
    school = getschool(request)
    sections  = None
    if grade != 0:
        sections = getSections(request, grade)
    
    grades =  getClasses(request) 
    selectedGrade = 'Select Grade'
    if grade != 0:
        selectedGrade = Class.objects.get(id= grade)
    context = {'sections': sections, 'school': school, 'grades': grades, 'selected_grade': selectedGrade}
    return render(request, 'sections.html',context)

@login_required(login_url='/login')
def registerclasses(request):
    pv_id_if_exist = request.GET.get('id')
    form = None
    if Class.objects.filter(id=pv_id_if_exist):
        form  = RegisterClassesForm(instance=Class.objects.filter(id=pv_id_if_exist)[0])
    else:
        form  = RegisterClassesForm()
    school = getschool(request)
    messages =[]
    if request.method == 'POST':
        if pv_id_if_exist != None:
            form = RegisterClassesForm(request.POST, instance=Class.objects.filter(id=pv_id_if_exist)[0])
        else:
            form = RegisterClassesForm(request.POST)
        if form.is_valid():
            form.save()
            if pv_id_if_exist != None:
                messages.append('Class Updated Successfully')
            else:
                messages.append('Class Added Successfully')
        
            
    context = {'form': form, 'school':school, 'messages': messages}
    return render(request, 'registerclass.html',context)

@login_required(login_url='/login')
def registersections(request):
    pv_id_if_exist = request.GET.get('id')
    form = None
    if Section.objects.filter(id=pv_id_if_exist):
        form  = RegisterSectionsForm(instance=Section.objects.filter(id=pv_id_if_exist)[0])
    else:
        form  = RegisterSectionsForm()
    school = getschool(request)
    messages =[]
    if request.method == 'POST':
        if pv_id_if_exist != None:
            form = RegisterSectionsForm(request.POST,instance=Section.objects.filter(id=pv_id_if_exist)[0])
        else:
            form = RegisterSectionsForm(request.POST)
        if form.is_valid():
            form.save()
            if pv_id_if_exist != None:
                messages.append('Section Updated Successfully')
            else:
                messages.append('Section Added Successfully')
        
            
    context = {'form': form, 'school':school, 'messages': messages}
    return render(request, 'registersections.html',context)

@login_required(login_url='/login')
def routine(request):
    school = getschool(request)
    context = {'school': school}
    return render(request, 'routine.html', context)

@login_required(login_url='/login')
def results(request):
    school = getschool(request)
    classes = getClasses(request)
    results = getResults(request)
    context = {'school': school, 'grades': classes, 'results': results}
    return render(request, 'results.html', context)

@login_required(login_url='/login')
def resultbuilder(request,id,grade):
    school = getschool(request)
    result = Result.objects.get(id=id)
    if request.method == 'POST':
        body = json.loads(request.body)
        result.resultsheet = body
        result.save()
        return JsonResponse('Updated' , safe=False)
    grade_ = Class.objects.get(id=grade)
    students = getStudents(request,grade)
    subjects = getSubjects(request,grade)
    sections = getSections(request,grade)
    context = {'school': school,'result_info': result, 'grade': grade_, 'students': students, 'subjects': subjects,'results': json.dumps(result.resultsheet),"sections": sections}
    return render(request, 'resultbuilder.html', context)



@login_required(login_url='/login')
def prepareresult(request,id,grade):
    school = getschool(request)
    result = Result.objects.get(id=id)
    if request.method == 'POST':
        body = json.loads(request.body)
        result.resultsheet = body
        result.save()
        return JsonResponse('Updated' , safe=False)
    grade_ = Class.objects.get(id=grade)
    students = getStudents(request,grade)
    subjects = getSubjects(request,grade)
    sections = getSections(request,grade)
    context = {'school': school,'result_info': result, 'grade': grade_, 'students': students, 'subjects': subjects,'results': json.dumps(result.resultsheet),"sections": sections}
    return render(request, 'prepareresult.html', context)