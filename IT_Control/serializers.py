from rest_framework import serializers
from .models import (
    StudentManagement,
    StaffManagement,
    CourseEnrollment,
)


class StudentManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentManagement
        fields = '__all__'


class StaffManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffManagement
        fields = '__all__'


class CourseEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseEnrollment
        fields = '__all__'