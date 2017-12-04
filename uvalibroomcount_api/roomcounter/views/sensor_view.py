from rest_framework import viewsets
from rest_framework.permissions import *
from rest_framework.response import Response
from roomcounter.models import *
from roomcounter.serializers import *


class SensorViewSet(viewsets.ModelViewSet):
    ''' The SensorViewSet class is a view that lists out all sensors.
    '''
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = sensor_model.Sensor.objects.all()
    serializer_class = sensor_serializer.SensorSerializer
