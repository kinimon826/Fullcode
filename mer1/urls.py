from django.urls import path
from .views import (
    BidzaiavkaCreateAPI,
    UslugasListAPI,
    ProjectListAPI,
    OsavatelListAPI,
    ComandaListAPI,
    LogoListAPI,
    NewsListAPI,
)

urlpatterns = [
    path('bidzaiavkas/', BidzaiavkaCreateAPI.as_view(), name='bidzaiavka-create'),
    path('uslugas/', UslugasListAPI.as_view(), name='uslugas-list'),
    path('projects/', ProjectListAPI.as_view(), name='projects-list'),
    path('osavatels/', OsavatelListAPI.as_view(), name='osavatels-list'),
    path('comandas/', ComandaListAPI.as_view(), name='comandas-list'),
    path('logos/', LogoListAPI.as_view(), name='logos-list'),
    path('news/', NewsListAPI.as_view(), name='news-list'),
]