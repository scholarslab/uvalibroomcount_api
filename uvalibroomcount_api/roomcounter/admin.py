from django.contrib import admin
from roomcounter.models import *
# Register your models here.
admin.site.register(building_model.Building)
admin.site.register(room_model.Room)
admin.site.register(sensor_model.Sensor)
admin.site.register(room_occupancy_model.RoomOccupancy)
admin.site.register(sensor_result_model.SensorResult)
