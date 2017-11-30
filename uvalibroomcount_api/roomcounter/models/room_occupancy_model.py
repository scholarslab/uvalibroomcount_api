from django.db import models
from django.contrib.gis.db.models import PolygonField
from . import room_model


class RoomOccupancy(models.Model):
    ''' The RoomOccupancy class is a model that defines which data is available in the RoomOccupancy table.
    '''
    date_created = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(room_model.Building, null=True, on_delete=models.CASCADE, related_name='room_occupancy')
    occupancy = models.IntegerField()
    date_updated = models.DateTimeField(null=True)
    archived = models.BooleanField(default=False)
    date_archived = models.DateTimeField(null=True)

    def __str__(self):
        return '%s %s' % (self.id, self.occupancy)
