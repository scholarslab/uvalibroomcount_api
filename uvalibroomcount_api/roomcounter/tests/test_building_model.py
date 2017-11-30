from django.test import TestCase
from django.urls import reverse
from roomcounter.models import *
from roomcounter.views import *

class TestBuildingModel(TestCase):
    """
    This class tests everything related to a building model
    - crud building
    - add room to building
    - get building hours
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_building_created(self):
        """
        Test that a building can be created
        """
        building = building_model.Building.create(
            building_name = 'Alderman Library',
            building_location = 'POINT(38.029306, -78.476678)'
        )
        self.assertIsInstance(building, building_model.Building)

    def test_building_deleted(self):
        pass

    def test_building_updated(self):
        pass
