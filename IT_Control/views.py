import requests
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from .models import (
    StudentManagement,
    StaffManagement,
    CourseEnrollment
)
from .serializers import (
    StudentManagementSerializer,
    CourseEnrollmentSerializer,
    StaffManagementSerializer
)


TELEGRAM_BOT_TOKEN = "8324481424:AAGF_6hOrGdyHOfjmVghOenVvQEEy3l8j7U"
TELEGRAM_CHAT_ID = "1727263622"


def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }
    try:
        requests.post(url, data=payload)
    except:
        pass



class CourseEnrollmentListView(generics.ListAPIView):
    queryset = CourseEnrollment.objects.all()
    serializer_class = CourseEnrollmentSerializer


class StudentManagementListView(generics.ListAPIView):
    queryset = StudentManagement.objects.all()
    serializer_class = StudentManagementSerializer



class StaffManagementCreateView(generics.CreateAPIView):
    queryset = StaffManagement.objects.all()
    serializer_class = StaffManagementSerializer

    def perform_create(self, serializer):
        job = serializer.save()


        position_label = next(
            (label for value, label in job.JOB_POSITIONS if value == job.position),
            job.position
        )

        text = (
            f"🆕 <b>Новая запись для управления персоналом</b>\n\n"
            f"<b>Кем работает:</b> {position_label}\n"
            f"<b>Телефон номер:</b> {job.phone_number}\n"
            f"<b>Email почта:</b> {job.email}\n"
            f"<b>Опыт работы:</b> {'Есть' if job.has_experience else 'Нет'}\n"
            f"<b>Сколько получает:</b> {job.salary}\n"
            f"<b>Уволен?:</b> {'Да' if job.is_terminated else 'Нет'}"
        )
        send_telegram_message(text)