from rest_framework import serializers
from .models import StudentModel


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'
