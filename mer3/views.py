from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import studentu, rabotau, cursu
from .serializers import (studentuSerializer, cursuSerializer, rabotauSerializer,)
import requests
import json
import datetime
import os



LOG_DIR = 'copy'
LOG_FILE_JSON = os.path.join(LOG_DIR, 'api_copy.json')

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)


def log_api_request(method, url_path, status_code, data=None):
    log_entry = {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "method": method,
        "url_path": url_path,
        "status_code": status_code,
        "request_data": data if method == 'POST' else None
    }
    data_list = []
    if os.path.exists(LOG_FILE_JSON):
        try:
            with open(LOG_FILE_JSON, 'r', encoding='utf-8') as f:
                content = f.read()
                if content:
                    data_list = json.loads(content)
        except (json.JSONDecodeError, FileNotFoundError):
            data_list = []
    data_list.append(log_entry)
    try:
        with open(LOG_FILE_JSON, 'w', encoding='utf-8') as f:
            json.dump(data_list, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"ЛОГГЕР ОШИБКА: Не удалось сохранить в файл: {e}")


TOKEN = "8324481424:AAGF_6hOrGdyHOfjmVghOenVvQEEy3l8j7U"
CHAT_ID = "1727263622"


def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }
    try:
        requests.post(url, data=payload)
    except:
        pass

class cursssList(APIView):
    def get(self, request):
        curses = cursu.objects.all()
        response_data = cursuSerializer(curses, many=True).data
        log_api_request(
            method='GET',
            url_path=request.path,
            status_code=status.HTTP_200_OK
        )
        return Response(response_data)



class studenstsList(APIView):
    def get(self, request):
        students = studentu.objects.all()
        response_data = studentuSerializer(students, many=True).data
        log_api_request(
            method='GET',
            url_path=request.path,
            status_code=status.HTTP_200_OK
        )
        return Response(response_data)


class rabotassList(APIView):
    serializer_class = rabotauSerializer
    def post(self, request):
        serializer = rabotauSerializer(data=request.data)
        if serializer.is_valid():
            job = serializer.save()
            text = (
                f"🆕 <b>администратор</b>\n\n"
                f"<b>Кем работает:</b> {job.Human}\n"
                f"<b>Телефон номер:</b> {job.number}\n"
                f"<b>Email почта:</b> {job.email}\n"
                f"<b>Опыт работы:</b> {'Есть' if job.test else 'Нет'}\n"
                f"<b>сколько получает:</b> {job.money}\n"
                f"<b>уволить?:</b> {job.paid}"
            )
            send_telegram_message(text)
            log_api_request(
                method='POST',
                url_path=request.path,
                status_code=status.HTTP_201_CREATED,
                data=request.data
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        log_api_request(
            method='POST',
            url_path=request.path,
            status_code=status.HTTP_400_BAD_REQUEST,
            data={'errors': serializer.errors, 'input_data': request.data}
        )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)