from rest_framework import viewsets
from rest_framework.permissions import *
from rest_framework.response import Response
from roomcounter.models import *
from roomcounter.serializers import *

# need a view to get all buildings, individual buildings, building hours, delete a building, update a building - needs permissions
class BuildingViewSet(viewsets.ModelViewSet):
    ''' The BuildingViewSet class is a view that lists out all buildings and details about a building.
    '''
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = building_model.Building.objects.all()
    serializer_class = building_serializer.BuildingSerializer
