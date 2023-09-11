import json

from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dronekit import connect, APIException
from . import constants
import dronekit
import socket
from . import VehicleSingleton
from .VehicleSingleton import MyVehicleSingleton


# Create your views here.


@api_view(['GET'])
def index(request):
    data = {
        'message': 'Hello World'
    }
    return Response(data, status.HTTP_200_OK)


@api_view(['POST', 'DELETE'])
def connect_drone(request):
    if request.method == 'POST':
        req_data = json.loads(request.body)
        port = req_data.get('port')
        data, status_code = connect_helper(port)
    else:
        data, status_code = disconnect()

    return Response(data, status_code)


def connect_helper(port):
    try:
        '''
        I probably shouldn't use a singleton because it's not stateless, 
        but I'm not sure how to vehicle fits with the REST API
        '''
        my_vehicle = MyVehicleSingleton(port)
        data = {'message': my_vehicle.vehicle.system_status.__str__()}
        status_code = status.HTTP_200_OK
    # Failed connection
    except OSError as e:
        data = {'message': 'connection error'}
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    # API Error
    except dronekit.APIException:
        data = {'message': 'timeout'}
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        pass
    # Other error
    except Exception as e:
        data = {'message': e.args}
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return data, status_code


def disconnect():
    my_vehicle = MyVehicleSingleton.get_instance()
    if my_vehicle is not None:
        my_vehicle.vehicle.close()
        MyVehicleSingleton.delete_instance()
    data = {'message': 'disconnected'}
    status_code = status.HTTP_200_OK
    return data, status_code

