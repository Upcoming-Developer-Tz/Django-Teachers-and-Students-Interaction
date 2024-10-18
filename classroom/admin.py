from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Statuses)
class StatusesAdmin(admin.ModelAdmin):
    list_display = Statuses.display_fields

@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    list_display = Teachers.display_fields

@admin.register(SchoolLevels)
class SchoolLevelsAdmin(admin.ModelAdmin):
    list_display = SchoolLevels.display_fields

@admin.register(SchoolClases)
class SchoolClasesAdmin(admin.ModelAdmin):
    list_display = SchoolClases.display_fields

@admin.register(Subjects)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = Subjects.display_fields

@admin.register(AssignToClasses)
class AssignToClassesAdmin(admin.ModelAdmin):
    list_display = AssignToClasses.display_fields

@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = Questions.display_fields

@admin.register(Answers)
class AnswersAdmin(admin.ModelAdmin):
    list_display = Answers.display_fields

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = Students.display_fields
