import re
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
    school = getschool(request)
    if not school:
        return redirect('/404')
    form  = None
    if type == 'student':
        form = RegisterStudentForm()
    elif type == 'staff':
        form = RegisterStaffForm()
    elif type == 'parents':
        form = RegisterParentsForm()
    if request.method == 'POST':
        if type == 'student':
            form = RegisterStudentForm(request.POST,request.FILES)
        elif type == 'staff':
            form = RegisterStaffForm(request.POST,request.FILES)
        elif type == 'parents':
            form = RegisterParentsForm(request.POST,request.FILES)
        
        if form.is_valid():
            form.save()
            if type == 'student':
                return redirect('/students')
            elif type == 'staff':
                return redirect('/staff')
            elif type == 'parents':
                return redirect('/parents')
            
        else:
            print('not valid')
        
    context = {'school': school, 'form': form}
    if type == 'student':
        context['classes'] = getClasses(request)
        context['sections'] = {}
    return render(request, 'register.html', context)

def profile(request):
    school = getschool(request)
    if not school:
        return redirect('/404')
    context ={'school': school}
    return render(request, 'profile.html', context)


def sections(request, grade):
    resp = [];
    data = getSections(request, grade)
    for d in data:
        resp.append({
            'name': d.section_name,
            'id': d.id
        })
    return JsonResponse(resp , safe=False)