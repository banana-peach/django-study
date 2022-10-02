from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['last_name', 'first_name','id']