from django.urls import path
from .views import (studenstsList, rabotassList, cursssList)

urlpatterns = [
    path("students/", studenstsList.as_view()),
    path("rabotas/", rabotassList.as_view()),
    path("curs/", cursssList.as_view()),
]
