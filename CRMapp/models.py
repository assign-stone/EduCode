from turtle import mode
from unicodedata import name
from django.db import models

# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=50)
    duration=models.IntegerField()
    fees=models.FloatField()
    class Meta:
        db_table='course'

class Subject(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    Course=models.ManyToManyField(Course)
    class Meta:
        db_table='subject'

class Batch(models.Model):
    StartDate=models.DateField()
    StartTime=models.TimeField()
    endTime=models.TimeField()
    course=models.ForeignKey(Course,on_delete=models.RESTRICT)
    class Meta:
        db_table='batch'

class Student(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    marks=models.FloatField()
    betch=models.ManyToManyField(Batch)
    class Meta:
        db_table='student'

class Faculty(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    salary=models.FloatField()
    qualification=models.CharField(max_length=50)
    skills=models.ManyToManyField(Subject)
    batches=models.ManyToManyField(Batch)
    class Meta:
        db_table='faculty'

class FeeRecord(models.Model):
    student=models.ForeignKey(Student,null=True,on_delete=models.SET_NULL)
    batch=models.ForeignKey(Batch,null=True,on_delete=models.SET_NULL)
    amount=models.FloatField()
    date=models.DateField()
    time=models.TimeField()
    mode=models.CharField(max_length=50)
    remarks=models.CharField(max_length=300)
    class Meta:
        db_table='fee_record'

class Admin(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    class Meta:
        db_table='admin'