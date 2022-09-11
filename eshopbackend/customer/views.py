import email
import json
from unicodedata import name
from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Customer
# Create your views here.
# @method_decorator(csrf_exempt, name='dispatch')
class UserStore(APIView):

    def post(self, request, format=None):
        name=request.data['name']
        email=request.data['email']
        if not Customer.objects.filter(email=email).exists():
            customer=Customer.objects.create(name=name,email=email)
            customer.save()
        return Response({'message':'User created.','code':10201}, status=status.HTTP_201_CREATED)