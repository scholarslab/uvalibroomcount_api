from django.db import models
from django.contrib.gis.db.models import PolygonField
from . import building_model


class Room(models.Model):
    ''' The Room class is a model that defines which data is available in the Room table.
    '''
    date_created = models.DateTimeField(auto_now_add=True)
    building = models.ForeignKey(building_model.Building, null=True, on_delete=models.CASCADE, related_name='rooms')
    # room_dimensions = PolygonField()
    room_name = models.CharField(max_length=200, blank=True)
    room_max_capacity = models.IntegerField()
    building_floor = models.CharField(max_length=100)
    # going to need to develop a way to check if room is open
    #also an update field?

    def __str__(self):
        return '%s %s' % (self.id, self.room_name)
