from django.contrib import admin
from .models import Student, Instructor, Course


class CourseAdmin(admin.ModelAdmin):
    fields = ['name', 'course_slug', 'instructor', 'students', 'start_date', 'end_date', 'description']

    list_display = ('name', 'instructor', 'start_date', 'end_date', 'description')

    list_filter =  ['instructor__name']

    search_fields = ['description', 'name']
    prepopulated_fields = {'course_slug': ('name',)}

admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Course, CourseAdmin)