from rest_framework import serializers
from roomcounter.models import *

class BuildingSerializer(serializers.HyperlinkedModelSerializer):
    ''' The BuildingSerializer class translates the Building models into other formats, in this case JSON by default.
    Method List:
    -Meta
    -create
    -update
    '''
    class Meta:
        model = building_model.Building
        fields = '__all__'
        depth = 1
