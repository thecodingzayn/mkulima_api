from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Test
from .serializers import TestSerializer

class TestView(APIView):
    def get(self, request):
        data = Test.objects.all()
        return Response(TestSerializer(data, many=True).data)
