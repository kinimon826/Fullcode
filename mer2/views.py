from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import student, work, Companymy, rabota, zaiavka
from .serializers import (studentSerializer, workSerializer, onasSerializer, cursSerializer, sertificatSerializer, CompanymySerializer, rabotaSerializer, zaiavkaSerializer)
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


class studentsList(APIView):
    def get(self, request):
        students = student.objects.all()
        response_data = studentSerializer(students, many=True).data
        log_api_request(
            method='GET',
            url_path=request.path,
            status_code=status.HTTP_200_OK
        )
        return Response(response_data)


class worksList(APIView):
    def get(self, request):
        workers = work.objects.all()
        response_data = workSerializer(workers, many=True).data
        log_api_request(
            method='GET',
            url_path=request.path,
            status_code=status.HTTP_200_OK
        )
        return Response(response_data)


class CompanymysList(APIView):
    def get(self, request):
        companies = Companymy.objects.all()
        response_data = CompanymySerializer(companies, many=True).data
        log_api_request(
            method='GET',
            url_path=request.path,
            status_code=status.HTTP_200_OK
        )
        return Response(response_data)


class zaiavkasList(APIView):
    serializer_class = zaiavkaSerializer
    def post(self, request):
        serializer = zaiavkaSerializer(data=request.data)
        if serializer.is_valid():
            form = serializer.save()
            msg = (
                f"📨 <b>заявка</b>\n\n"
                f"<b>Телефон номер:</b> {form.number}\n"
                f"<b>Email почта:</b> {form.email}\n"
                f"<b>Описание:</b> {form.text}"
            )
            send_telegram_message(msg)
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


class rabotasList(APIView):
    serializer_class = rabotaSerializer
    def post(self, request):
        serializer = rabotaSerializer(data=request.data)
        if serializer.is_valid():
            job = serializer.save()
            text = (
                f"🆕 <b>заявка на работу</b>\n\n"
                f"<b>Кем хочет устроиться:</b> {job.Human}\n"
                f"<b>Телефон номер:</b> {job.number}\n"
                f"<b>Email почта:</b> {job.email}\n"
                f"<b>Опыт работы:</b> {'Есть' if job.test else 'Нет'}\n"
                f"<b>хочет в месяц:</b> {job.money}\n"
                f"<b>Интересует:</b> {job.interest}"
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


class sertificatsList(APIView):
    def get(self, request):
        sert = sertificat.objects.all()
        response_data = sertificatSerializer(sert, many=True).data
        log_api_request(
            method='GET',
            url_path=request.path,
            status_code=status.HTTP_200_OK
        )
        return Response(response_data)

class onassList(APIView):
    def get(self, request):
        onases = onas.objects.all()
        response_data = onasSerializer(onases, many=True).data
        log_api_request(
            method='GET',
            url_path=request.path,
            status_code=status.HTTP_200_OK
        )
        return Response(response_data)

class curssList(APIView):
    def get(self, request):
        curses = curs.objects.all()
        response_data = cursSerializer(curses, many=True).data
        log_api_request(
            method='GET',
            url_path=request.path,
            status_code=status.HTTP_200_OK
        )
        return Response(response_data)