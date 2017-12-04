from django.db import models
from . import sensor_model


class SensorResult(models.Model):
    ''' The Sensor Result class is a model that defines which data is available in the Sensor Result table.
    '''
    date_recorded = models.DateTimeField(auto_now_add=True)
    sensor = models.ForeignKey(sensor_model.Sensor, null=True, on_delete=models.CASCADE, related_name='sensor_results')
    count_up = models.IntegerField(default=0)
    count_down = models.IntegerField(default=0)

    # boolean field here is stand-in. Need to decide if we want to use 0 or 1, or some type of integer or word to represent positive and negative results

    def __str__(self):
        return '%s %s %s %s' % (self.id, self.count_down, self.count_up, self.date_recorded)
