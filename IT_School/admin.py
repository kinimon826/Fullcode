from django.contrib import admin
from .models import (
    Student,
    Worker,
    Company,
    JobApplication,
    Application,
    AboutUsItem,
    Certificate,
    Course
)

admin.site.register(Student)
admin.site.register(Worker)
admin.site.register(Company)
admin.site.register(JobApplication)
admin.site.register(Application)
admin.site.register(AboutUsItem)
admin.site.register(Certificate)
admin.site.register(Course)