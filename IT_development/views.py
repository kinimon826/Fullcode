import requests
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import (
    ContactRequest,
    Service,
    Project,
    Founder,
    TeamMember,
    Logo,
    SiteSettings
)
from .serializers import (
    ContactRequestSerializer,
    ServiceSerializer,
    ProjectSerializer,
    FounderSerializer,
    TeamMemberSerializer,
    LogoSerializer,
    SiteSettingsSerializer
)

TELEGRAM_TOKEN = "8324481424:AAGF_6hOrGdyHOfjmVghOenVvQEEy3l8j7U"
CHAT_ID = "1727263622"


def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    try:
        requests.post(url, data=payload)
    except:
        pass




class ContactRequestCreateView(generics.CreateAPIView):
    queryset = ContactRequest.objects.all()
    serializer_class = ContactRequestSerializer

    def perform_create(self, serializer):
        bid = serializer.save()
        message = (
            f"📌 <b>НОВАЯ ЗАЯВКА НА КОНТАКТ!</b>\n"
            f"Имя: {bid.first_name}\n"
            f"Фамилия: {bid.last_name}\n"
            f"Телефон: {bid.phone_number}\n"
        )
        send_telegram_message(message)



class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer



class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer



class FounderListView(generics.ListAPIView):
    queryset = Founder.objects.all()
    serializer_class = FounderSerializer



class TeamMemberListView(generics.ListAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer



class LogoListView(generics.ListAPIView):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer



class SiteSettingsListView(generics.ListAPIView):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer