from django.db import models
from django.contrib.gis.db.models import PointField
from . import room_model


class Sensor(models.Model):
    ''' The Sensor class is a model that defines which data is available in the Sensor table.
    '''
    date_created = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(room_model.Room, null=True, on_delete=models.CASCADE, related_name='sensors')
    sensor_location = PointField()
    active = models.BooleanField(default=True)
    # do we want to give sensors names for ease of identifying them? Like periodical_room_sensor_one?

    def __str__(self):
        return '%s %s' % (self.id, self.active)
