from django.contrib import admin
from .models import *

admin.site.register(StudentId)
admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(Student)

class SubjectMarksDisplay(admin.ModelAdmin):
    list_display = ['student', 'subject', 'marks']
admin.site.register(SubjectMarks, SubjectMarksDisplay)