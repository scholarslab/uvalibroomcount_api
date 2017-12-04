from django.db import models
from django.contrib.gis.db.models import PolygonField
from . import room_model


class RoomOccupancy(models.Model):
    ''' The RoomOccupancy class is a model that defines which data is available in the RoomOccupancy table.
    '''
    date_created = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(room_model.Room, null=True, on_delete=models.CASCADE, related_name='room_occupancy')
    occupancy = models.IntegerField(default=0)
    archived = models.BooleanField(default=False)
    date_archived = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.id, self.occupancy)
