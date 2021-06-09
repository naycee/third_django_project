from django.contrib import admin
from .models import Student, School, Faculty, Department, Certificate_type, Grade

# Register your models here.
admin.site.register(Student)
admin.site.register(School)
admin.site.register(Department)
admin.site.register(Faculty)
admin.site.register(Certificate_type)
admin.site.register(Grade)
