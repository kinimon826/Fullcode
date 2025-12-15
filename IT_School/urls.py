from django.urls import path
from .views import (
    StudentListCreateView,
    WorkerListView,
    CompanyListView,
    ApplicationCreateView,
    JobApplicationCreateView,
    CourseListView,
    AboutUsItemListView,
    CertificateListView
)

urlpatterns = [
    path("students/", StudentListCreateView.as_view(), name='student-list-create'),
    path("workers/", WorkerListView.as_view(), name='worker-list'),
    path("companies/", CompanyListView.as_view(), name='company-list'),
    path("applications/", ApplicationCreateView.as_view(), name='application-create'),
    path("jobapplications/", JobApplicationCreateView.as_view(), name='jobapplication-create'),
    path("courses/", CourseListView.as_view(), name='course-list'),
    path("aboutus/", AboutUsItemListView.as_view(), name='aboutus-list'),
    path("certificates/", CertificateListView.as_view(), name='certificate-list'),
]