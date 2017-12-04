from rest_framework import serializers
from roomcounter.models import *

class RoomOccupancySerializer(serializers.HyperlinkedModelSerializer):
    ''' The RoomOccupancySerializer class translates the Room Occupancy models into other formats, in this case JSON by default.
    Method List:
    -Meta
    -create
    -update
    '''
    class Meta:
        model = room_occupancy_model.RoomOccupancy
        fields = '__all__'
        depth = 2
