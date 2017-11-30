from django.test import TestCase
from django.urls import reverse
from roomcounter.models import *
from roomcounter.views import *

class TestSensorResultModel(TestCase):
    """
    This class tests everything related to a sensor result model
    - crud sensor result
    """
    def setUp(self):
        self.building = building_model.Building.create(
            building_name = 'Alderman Library',
            building_location = 'POINT(38.029306, -78.476678)'
        )
        self.room = room_model.Room.objects.create(
            building = building,
            room_name = 'Periodicals Room',
            room_max_capacity = 40,
            building_floor = 3,
        )
        self.sensor = sensor_model.Sensor.objects.create(
            room = self.room,
            sensor_location = 'POINT(38.029306, -78.476678)'
        )
        self.sensor_result = sensor_result_model.SensorResult.objects.create(
            sensor = self.sensor,
            result = True
        )

    def tearDown(self):
        del self.building
        del self.room
        del self.sensor

    def test_sensor_result_created(self):
        """
        Test that a sensor result can be created
        """
        self.assertEqual(sensor_result_model.SensorResult.objects.get(sensor=self.sensor).pk, self.sensor_result.pk)
