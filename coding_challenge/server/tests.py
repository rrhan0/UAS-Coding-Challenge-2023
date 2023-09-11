import json
import dronekit_sitl
from django.test import TestCase
from rest_framework.test import APIClient



class DroneTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.sitl = dronekit_sitl.start_default()
        self.connection_string = self.sitl.connection_string()

    def tearDown(self):
        self.sitl.stop()

    def test_connect_drone_success(self):
        payload = {'port': 5760}
        response = self.client.post('/api/server/index/connect', payload, format='json')

