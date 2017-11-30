from rest_framework import serializers
from roomcounter.models import *

class SensorResultSerializer(serializers.HyperlinkedModelSerializer):
    ''' The SensorResultSerializer class translates the Sensor Result models into other formats, in this case JSON by default.
    Method List:
    -Meta
    -create
    -update
    '''
    class Meta:
        model = sensor_result_model.SensorResult
        fields = '__all__'
        depth = 1
