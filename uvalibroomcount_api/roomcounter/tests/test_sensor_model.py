from django.test import TestCase
from django.urls import reverse
from roomcounter.models import *
from roomcounter.views import *

class TestSensorModel(TestCase):
    """
    This class tests everything related to a sensor model
    - crud sensor
    - add sensor to room
    """
    def setUp(self):
        self.building = building_model.Building.create(
            building_name = 'Alderman Library',
            building_location = 'POINT(38.029306, -78.476678)'
        )
        self.room = room_model.Room.objects.create(
            building = self.building,
            room_name = 'Periodicals Room',
            room_max_capacity = 40,
            building_floor = 3,
        )
        self.sensor = sensor_model.Sensor.objects.create(
            room = self.room,
            sensor_location = 'POINT(38.029306, -78.476678)'
        )

    def tearDown(self):
        del self.building
        del self.room
        del self.sensor

    def test_sensor_created(self):
        """
        Test that a sensor can be created
        """
        self.assertEqual(sensor_model.Sensor.objects.get(room=self.room).pk, self.sensor.pk)

    def test_sensor_deleted(self):
        """
        Test that a sensor can be deleted
        """
        new_sensor = sensor_model.Sensor.objects.create(
            room = self.room,
            sensor_location = 'POINT(38.029306, -78.476678)'
        )
        self.assertIsInstance(new_sensor, sensor_model.Sensor)
        new_sensor.delete()
        all_sensors = sensor_model.Sensor.objects.all(room=self.room)
        self.assertNotIn(new_sensor, all_sensors)

    def test_sensor_updated(self):
        """
        Test that a sensor can be updated
        """
        self.sensor.active = False
        self.sensor.save()
        self.assertFalse(self.sensor.active)
