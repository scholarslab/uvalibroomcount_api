from django.test import TestCase
from django.urls import reverse
from roomcounter.models import *
from roomcounter.views import *
from datetime import datetime


class TestRoomOccupancyModel(TestCase):
    """
    This class tests everything related to a room occupancy model
    - crud room occupancy

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
        self.room_occupancy = room_occupancy_model.RoomOccupancy.objects.create(
            room = self.room,
            occupancy = 10,
        )
    def tearDown(self):
        del self.building
        del self.room
        del self.room_occupancy

    def test_room_occupancy_created(self):
        """
        Test that a room occupancy can be created
        """
        assertEqual(room_occupancy_model.RoomOccupancy.objects.get(room=self.room).pk, self.room_occupancy.pk)

    # def test_room_occupancy_updated(self):
    #     """
    #     Test that a room occcupancy can be updated
    #     """
    #     self.room_occupancy.occupancy = self.room_occupancy.occupancy + 1
    #     self.room_occupancy.save()
    #     self.room_occupancy.date_archived = datetime.now().time()
    #     assertEqual(self.room_occupancy.occupancy, 11)

    def test_room_occupancy_archived(self):
        """
        Test that a room occcupancy can be archived
        """
        self.room_occupancy.occupancy = self.room_occupancy.occupancy + 1
        self.room_occupancy.archived = True
        self.room_occupancy.date_archived = datetime.now().time()
        self.room_occupancy.save()
        assertEqual(self.room_occupancy.occupancy, 11)
        assertTrue(self.room_occupancy.archived)
