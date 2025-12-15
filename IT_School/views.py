from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
import requests

from .models import (
    Student,
    Worker,
    Company,
    JobApplication,
    Application,
    Certificate,
    AboutUsItem,
    Course
)
from .serializers import (
    StudentSerializer,
    WorkerSerializer,
    AboutUsItemSerializer,
    CourseSerializer,
    CertificateSerializer,
    CompanySerializer,
    JobApplicationSerializer,
    ApplicationSerializer
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


class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def perform_create(self, serializer):
        student_instance = serializer.save()

        message = (
            f"*{'НОВЫЙ СТУДЕНТ СОЗДАН!'}\n\n"
            f"{'Имя'}: *{student_instance.first_name} {student_instance.last_name}*\n"
            f"{'Возраст'}: {student_instance.age}\n"
            f"{'Язык'}: {student_instance.study_language}\n"
            f"{'Оплата'}: {'✅ Оплачено' if student_instance.is_paid else '❌ Не оплачено'}*"
        )

        send_telegram_message(message)


class WorkerListView(generics.ListAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class CompanyListView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CertificateListView(generics.ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class AboutUsItemListView(generics.ListAPIView):
    queryset = AboutUsItem.objects.all()
    serializer_class = AboutUsItemSerializer


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ApplicationCreateView(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def perform_create(self, serializer):
        form = serializer.save()
        msg = (
            f"📨 <b>Новая Заявка от клиента</b>\n\n"
            f"<b>Телефон номер:</b> {form.phone_number}\n"
            f"<b>Email почта:</b> {form.email}\n"
            f"<b>Описание:</b> {form.text}"
        )
        send_telegram_message(msg)


class JobApplicationCreateView(generics.CreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer

    def perform_create(self, serializer):
        job = serializer.save()

        human_label = next(
            (label for value, label in job.JOB_POSITIONS if value == job.desired_position),
            job.desired_position
        )

        text = (
            f"🆕 <b>Новая Заявка на работу</b>\n\n"
            f"<b>Кем хочет устроиться:</b> {human_label}\n"
            f"<b>Телефон номер:</b> {job.phone_number}\n"
            f"<b>Email почта:</b> {job.email}\n"
            f"<b>Опыт работы:</b> {'Есть' if job.has_experience else 'Нет'}\n"
            f"<b>Ожидаемая зарплата:</b> {job.salary_expectation}\n"
            f"<b>Интересует:</b> {job.interest}"
        )
        send_telegram_message(text)