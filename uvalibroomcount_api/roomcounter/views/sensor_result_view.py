from rest_framework import viewsets
from rest_framework.permissions import *
from rest_framework.response import Response
from roomcounter.models import *
from roomcounter.serializers import *


class SensorResultViewSet(viewsets.ModelViewSet):
    ''' The SensorResultViewSet class is a view that lists out all sensor results.
    '''
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = sensor_result_model.SensorResult.objects.all()
    serializer_class = sensor_result_serializer.SensorResultSerializer
