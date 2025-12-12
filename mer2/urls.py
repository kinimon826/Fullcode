from django.urls import path
from .views import (studentsList, worksList, CompanymysList, zaiavkasList, rabotasList, onassList, sertificatsList, curssList)

urlpatterns = [
    path("students/", studentsList.as_view()),
    path("works/", worksList.as_view()),
    path("Companymys/", CompanymysList.as_view()),
    path("zaiavkas/", zaiavkasList.as_view()),
    path("rabotas/", rabotasList.as_view()),
    path("curs/", curssList.as_view()),
    path("onas/", onassList.as_view()),
    path("sertificat/", sertificatsList.as_view())
]
