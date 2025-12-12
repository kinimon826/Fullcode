from rest_framework import serializers
from .models import bidzaiavka, Uslugi, project, Osavatel, Comanda, Logo, News


class BidzaiavkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = bidzaiavka
        fields = '__all__'


class UslugiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uslugi
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = project
        fields = '__all__'


class OsavatelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Osavatel
        fields = '__all__'


class ComandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comanda
        fields = '__all__'


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'