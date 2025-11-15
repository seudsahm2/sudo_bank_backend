from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from loguru import logger
# Create your views here.

class TestLogging(View):
    def get(self,request):
        logger.debug("this is a debug message")
        logger.info("this is a info message")
        logger.warning("this is a warning message")
        logger.error("this is a error message")
        logger.critical("this is a critical message")
        return JsonResponse({"message":"Logging test completed"})