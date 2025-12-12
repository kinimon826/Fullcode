from rest_framework import serializers
from .models import (
    student, work, Companymy, rabota, zaiavka,
    onas, curs, sertificat
)


class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'


class workSerializer(serializers.ModelSerializer):
    class Meta:
        model = work
        fields = '__all__'


class CompanymySerializer(serializers.ModelSerializer):
    class Meta:
        model = Companymy
        fields = '__all__'


class rabotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = rabota
        fields = '__all__'


class zaiavkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = zaiavka
        fields = '__all__'



class onasSerializer(serializers.ModelSerializer):
    class Meta:
        model = onas
        fields = '__all__'


class cursSerializer(serializers.ModelSerializer):
    class Meta:
        model = curs
        fields = '__all__'


class sertificatSerializer(serializers.ModelSerializer):
    class Meta:
        model = sertificat
        fields = '__all__'
