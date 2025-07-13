from django.contrib import admin
from .models import StudentModel, FacultyModel, EmployeeModel

admin.site.register(StudentModel)
admin.site.register(FacultyModel)
admin.site.register(EmployeeModel)
