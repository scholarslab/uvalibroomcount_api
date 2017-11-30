from django.db import models
from django.contrib.gis.db.models import PointField


class Building(models.Model):
    ''' The Building class is a model that defines which data is available in the Building table.
    '''
    date_created = models.DateTimeField(auto_now_add=True)
    building_name = models.CharField(max_length=200, blank=True)
    building_location = PointField()
    # going to need to develop a way to check if room is open
    #also an update field?

    def __str__(self):
        return '%s %s' % (self.id, self.building_name)
