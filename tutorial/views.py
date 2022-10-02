import json

from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from tutorial.models import Student
from tutorial.serializers import StudentSerializer


# from rest_framework.generics import ListAPIView


class StudentView(APIView):
    def get(self, request, *args, **kwargs):
        id = request.GET.get("id")
        print("Using the get method to excute!")
        print(id)
        res = Student.objects.filter(pk=id)
        data = Student.objects.all().values('last_name', 'first_name')
        data = list(data)
        ret = json.dumps(data)
        serializer_class = StudentSerializer(res, many=True)

        return Response(serializer_class.data)
        # return HttpResponse(ret)

    def post(self, request, *args, **kwargs):
        post_body = request.POST
        result = json.dumps(post_body)
        result = json.loads(result)
        print(result)
        name = result["name"]
        last = result["last"]
        res = Student.objects.create(first_name=name, last_name=last)

        return HttpResponse("ok")

        # Student.objects.create()
