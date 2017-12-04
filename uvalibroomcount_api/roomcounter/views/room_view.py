from rest_framework import viewsets
from rest_framework.permissions import *
from rest_framework.response import Response
from roomcounter.models import *
from roomcounter.serializers import *


class RoomViewSet(viewsets.ModelViewSet):
    ''' The RoomViewSet class is a view that lists out all rooms and details about a room.
    '''
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = room_model.Room.objects.all()
    serializer_class = room_serializer.RoomSerializer
