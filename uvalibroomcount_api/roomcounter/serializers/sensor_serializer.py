from rest_framework import serializers
from roomcounter.models import *

class SensorSerializer(serializers.HyperlinkedModelSerializer):
    ''' The SensorSerializer class translates the Sensor models into other formats, in this case JSON by default.
    Method List:
    -Meta
    -create
    -update
    '''
    class Meta:
        model = sensor_model.Sensor
        fields = '__all__'
        depth = 2
