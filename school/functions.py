from .models import *
from datetime import datetime
def getschool(request):
    schools =  School.objects.filter(user = request.user)
    school = None
    if schools:
        school = schools[0]
    return school

def getClasses(request):
    return Class.objects.filter(school = getschool(request)).all()


def getAvailableRollNo(grade=1):
    print(grade)
    rollnos = ()
    
    for i in range(50):
        val = ((i, i),)
        rollnos = rollnos + val
        
    print(rollnos)
    return rollnos


def getSections(request, grade_id):
    grade = Class.objects.get(id=grade_id)
    return Section.objects.filter(grade = grade).all()

def getStudents(request, grade=None):
    students = None
    if grade != None:
        students = Student.objects.filter(school = getschool(request)).all().filter(grade=grade)
    else:
        students = Student.objects.filter(school = getschool(request)).all()
    return students

def getStaffs(request):
    return Staff.objects.filter(school = getschool(request)).all()

def getParents(request):
    return Parent.objects.filter(school = getschool(request)).all()

def days_between(d1, d2):
    return (d1 - d2).days

def getPositions(request):
    return StaffPossition.objects.filter(school = getschool(request)).all()


def getSubjects(request, grade=None):
    subjects = None
    if grade != None:
        subjects = Subject.objects.filter(school = getschool(request)).all().filter(grade=grade)
    else:
        subjects = Subject.objects.filter(school = getschool(request)).all()
    return subjects


def getResults(request):
    return Result.objects.filter(school = getschool(request)).all()