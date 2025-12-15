from django.urls import path
from .views import (
    StudentManagementListView,
    StaffManagementCreateView,
    CourseEnrollmentListView
)

urlpatterns = [
    path("students/", StudentManagementListView.as_view(), name='student-management-list'),
    path("staff/", StaffManagementCreateView.as_view(), name='staff-management-create'),
    path("course/", CourseEnrollmentListView.as_view(), name='course-enrollment-list'),
]