import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import bidzaiavka, Uslugi, project, Osavatel, Comanda, Logo, News
from .serializers import (
    BidzaiavkaSerializer, UslugiSerializer,
    ProjectSerializer, OsavatelSerializer,
    ComandaSerializer, LogoSerializer,
    NewsSerializer
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
    requests.post(url, data=payload)




class BidzaiavkaCreateAPI(APIView):
    serializer_class = BidzaiavkaSerializer
    def post(self, request):
        serializer = BidzaiavkaSerializer(data=request.data)
        if serializer.is_valid():
            bid = serializer.save()
            message = (
                f"📌 <b>НОВАЯ ЗАЯВКА (bidzaiavka)!</b>\n"
                f"Имя: {getattr(bid, 'first_name', 'N/A')}\n"
                f"Телефон: {getattr(bid, 'age', 'N/A')}\n"
            )
            send_telegram_message(message)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UslugasListAPI(APIView):
    def get(self, request):
        services = Uslugi.objects.all()
        serializer = UslugiSerializer(services, many=True)
        return Response(serializer.data)

class ProjectListAPI(APIView):
    def get(self, request):
        projects = project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

class OsavatelListAPI(APIView):
    def get(self, request):
        founders = Osavatel.objects.all()
        serializer = OsavatelSerializer(founders, many=True)
        return Response(serializer.data)

class ComandaListAPI(APIView):
    def get(self, request):
        team = Comanda.objects.all()
        serializer = ComandaSerializer(team, many=True)
        return Response(serializer.data)

class LogoListAPI(APIView):
    def get(self, request):
        logos = Logo.objects.all()
        serializer = LogoSerializer(logos, many=True)
        return Response(serializer.data)

class NewsListAPI(APIView):
    def get(self, request):
        news_items = News.objects.all()
        serializer = NewsSerializer(news_items, many=True)
        return Response(serializer.data)