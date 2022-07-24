from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Admin,Subject,Course

# Create your views here.
def openloginForm(request):
    if request.session.get('adminid'):
        return redirect('/dashboard') 
    else:
        return render(request,'login.html')

def login(request):
    phone=request.POST['phone']
    passward=request.POST['password']
    result=Admin.objects.filter(phone=phone,password=passward)
    if result:
        dataList=result.values()
        request.session['adminid']=dataList[0]['id']
        return redirect("/dashboard")
    else:
        return render(request,"login.html",{"error":"Invalid UserId and password"})

def openDashboard(request):
    if request.session.get('adminid'):
        loggedInAdminId=request.session.get('adminid')
        admin=Admin.objects.get(id=loggedInAdminId)
        return render(request,'dashboard.html',{"admin":admin})
    else:
        return redirect('/')

def logout(request):
    del request.session['adminid']
    return redirect("/")

def openSubjectForm(request):
    if request.session.get('adminid'):
        loggedInAdminId=request.session.get('adminid')
        admin=Admin.objects.get(id=loggedInAdminId)
        return render(request,'AddSubjects.html',{"admin":admin})
    else:
        return redirect('/')

def openCoursesForm(request):
    if request.session.get('adminid'):
        loggedInAdminId=request.session.get('adminid')
        admin=Admin.objects.get(id=loggedInAdminId)
        return render(request,'addCourses.html',{"admin":admin})
    else:
        return redirect('/')

def openSubjectsList(request):
    if request.session.get('adminid'):
        loggedInAdminId=request.session.get('adminid')
        admin=Admin.objects.get(id=loggedInAdminId)
        subjects=Subject.objects.all()
        return render(request,'ViewSubjects.html',{"subjects":subjects,"admin":admin})
    else:
        return redirect('/')
        

def addSubject(request):
    subject=Subject()
    subject.name=request.POST['name']
    subject.description=request.POST['description']
    subject.save()
    return HttpResponse("Subject insereted !")

def openCoursesList(request):
    if request.session.get('adminid'):
        loggedInAdminId=request.session.get('adminid')
        admin=Admin.objects.get(id=loggedInAdminId)
        courses=Course.objects.all()
        return render(request,'viewCourses.html',{"courses":courses,"admin":admin})
    else:
        return redirect('/')
        

def addCourses(request):
    course=Course()
    course.name=request.POST['name1']
    course.duration=request.POST['duration']
    course.fees=request.POST['fees']
    course.save()
    return HttpResponse("Courses insereted")

def deleteSubject(request,id):
    subject=Subject.objects.get(id=id)
    subject.delete()
    return redirect("/viewsubjects")

def openEditForm(request,id):
    subject=Subject.objects.get(id=id)
    return render(request,"updateSubject.html",{"subs":subject})

def updateSubject(request,id):
    subject=Subject.objects.get(id=id)
    subject.name=request.POST['name']
    subject.description=request.POST['description']
    subject.save()
    return HttpResponse("Subject insereted !")

def deleteCourse(request,id):
    course=Course.objects.get(id=id)
    course.delete()
    return redirect("/viewcourses")

def openEditFormCourse(request,id):
    course=Course.objects.get(id=id)
    return render(request,"updateCourse.html",{"coursess":course})

def updateCourses(request,id):
    course=Course.objects.get(id=id)
    course.name=request.POST['name1']
    course.duration=request.POST['duration']
    course.fees=request.POST['fees']
    course.save()
    return HttpResponse("Courses insereted")
