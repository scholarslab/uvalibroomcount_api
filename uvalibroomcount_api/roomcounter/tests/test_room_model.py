from django.test import TestCase
from django.urls import reverse
from roomcounter.models import *
from roomcounter.views import *

class TestRoomModel(TestCase):
    """
    This class tests everything related to a room model
    - crud room
    - add room to building
    - get room hours
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

    def tearDown(self):
        del self.building
        del self.room

    def test_room_created(self):
        """
        Test that a room can be created
        """
        self.assertEqual(room_model.Room.objects.get(building=self.building).pk, self.room.pk)

    def test_room_deleted(self):
        """
        Test that a room can be deleted
        """
        new_room = room_model.Room.objects.create(
            building = self.building,
            room_name = 'Periodicals Room',
            room_max_capacity = 40,
            building_floor = 3,
        )
        self.assertIsInstance(new_room, room_model.Room)
        new_room.delete()
        all_rooms = room_model.Room.objects.all(building=self.building)
        self.assertNotIn(new_room, all_rooms)

    def test_room_updated(self):
        """
        Test that a room can be updated
        """
        self.room.floor = 4
        self.room.save()
        self.assertEqual(self.room.floor, 4)
