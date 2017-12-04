from rest_framework import viewsets
from rest_framework.permissions import *
from rest_framework.response import Response
from roomcounter.models import *
from roomcounter.serializers import *


class RoomOccupancyViewSet(viewsets.ModelViewSet):
    ''' The RoomOccupancyViewSet class is a view that details a room's occupancy.
    '''
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = room_occupancy_model.RoomOccupancy.objects.all()
    serializer_class = room_occupancy_serializer.RoomOccupancySerializer
