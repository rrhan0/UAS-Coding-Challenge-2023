import json

from django.shortcuts import render
from django.http import JsonResponse
from dronekit import connect
from . import constants
# Create your views here.


def index(request):
    data = {
        'message': 'Hello World'
    }
    return JsonResponse(data)


def connect_drone(request):
    port = 5760
    vehicle = connect(ip=f'{constants.DRONE_IP}:{port}', wait_ready=True)
    data = {'state': vehicle.system_status.__str__()}
    return JsonResponse(data)



