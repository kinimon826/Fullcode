from rest_framework import serializers
from .models import (
    studentu, rabotau, cursu,
)


class studentuSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentu
        fields = '__all__'

class rabotauSerializer(serializers.ModelSerializer):
    class Meta:
        model = rabotau
        fields = '__all__'

class cursuSerializer(serializers.ModelSerializer):
    class Meta:
        model = cursu
        fields = '__all__'