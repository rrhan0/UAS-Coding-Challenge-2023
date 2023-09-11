from dronekit import connect
from threading import Lock
from . import constants
from dronekit import connect


class Singleton (type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyVehicle(metaclass=Singleton):
    def __init__(self, port):
        self.vehicle = connect(ip=f'{constants.DRONE_IP}:{port}', wait_ready=True)


class MyVehicleSingleton(MyVehicle, metaclass=Singleton):
    @classmethod
    def get_instance(cls):
        return cls._instances.get(cls, None)

    @classmethod
    def delete_instance(cls):
        cls._instances = {}
