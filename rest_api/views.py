# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.decorators.csrf import  csrf_exempt
from django.utils.decorators import method_decorator

# from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

import logging
from logging.config import fileConfig

# Create your views here.
from django.views.decorators.csrf import  csrf_exempt
from django.utils.decorators import method_decorator

# from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
import logging
from logging.config import fileConfig
from .serializers import testSerializers

# logging configuration for streaming handler
fileConfig('./logging_config_stream.ini') 
logger = logging.getLogger()

# you can use a filerotator to save the logs into files and to avoid the disk saturation
# you can also write a configuration file that hand both the streaming and the filerotator
# fileConfig('./logging_config_stream.ini') 
# logger = logging.getLogger()

@method_decorator(csrf_exempt, name = 'dispatch')
class handling_request_view(APIView):
    parser_classes = (MultiPartParser,FormParser,JSONParser)

    def get(self, request, *args, **kwargs):
        logger.info("The GET Request was used")
        results = testSerializers(request.data, many=True).data
        # Here I just return what I receive you can manipulation,
        # You can what ever you want with the receive data and return the results you want
        return Response(results)

    def post(self, request, *args, **kwargs):
        logger.info("The POST Request was used")
        return Response("This is a Post Request")