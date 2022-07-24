from django.urls import path
from . import views
urlpatterns=[
    path('',views.openloginForm),
    path('dashboard',views.openDashboard),
    path('login',views.login),
    path('Logout',views.logout),
    path('subjectForm',views.openSubjectForm),
    path('courseForm',views.openCoursesForm),
    path('viewsubjects',views.openSubjectsList),
    path('addsubject',views.addSubject),
    path('viewcourses',views.openCoursesList),
    path('addcourses',views.addCourses),
    path('delete/<int:id>',views.deleteSubject),
    path('edit/<int:id>',views.openEditForm),
    path('update/<int:id>',views.updateSubject),
    path('deleteC/<int:id>',views.deleteCourse),
    path('editC/<int:id>',views.openEditFormCourse),
    path('updateC/<int:id>',views.updateCourses),
]