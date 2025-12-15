from django.contrib import admin
from .models import (
    CourseEnrollment,
    StudentManagement,
    StaffManagement
)


admin.site.register(CourseEnrollment)
admin.site.register(StudentManagement)
admin.site.register(StaffManagement)