from django.db import models
from django.urls import reverse, reverse_lazy


class Instructor(models.Model):
    name = models.CharField('Instructor Name', max_length=100)
    specialization = models.CharField('Subject Matter Expert', max_length=200)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    college = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField('Course Name', max_length=150)
    start_date = models.DateTimeField('Course Start Date')
    instructor = models.ForeignKey(Instructor, on_delete=models.DO_NOTHING)
    students = models.ManyToManyField(Student)
    description = models.TextField(blank=True)
    end_date = models.DateTimeField('Course End Date')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('course_details', args=[str(self.id)])