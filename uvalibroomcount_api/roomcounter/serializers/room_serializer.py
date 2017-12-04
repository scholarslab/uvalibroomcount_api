from rest_framework import serializers
from roomcounter.models import *

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    ''' The RoomSerializer class translates the Room models into other formats, in this case JSON by default.
    Method List:
    -Meta
    -create
    -update
    '''
    class Meta:
        model = room_model.Room
        fields = '__all__'
        depth = 2
