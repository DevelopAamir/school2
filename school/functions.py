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


def getSections(request, grade_id):
    grade = Class.objects.get(id=grade_id)
    return Section.objects.filter(grade = grade).all()

def getStudents(request):
    return Student.objects.filter(school = getschool(request)).all()

def getStaffs(request):
    return Staff.objects.filter(school = getschool(request)).all()

def getParents(request):
    return Parent.objects.filter(school = getschool(request)).all()

def days_between(d1, d2):
    return (d1 - d2).days

def getPositions(request):
    return StaffPosstion.objects.filter(school = getschool(request)).all()