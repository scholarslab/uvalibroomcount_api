"""uvalibroomcount_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from roomcounter.views import *
from rest_framework.routers import DefaultRouter
from roomcounter.admin import *

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'buildings', building_view.BuildingViewSet)
router.register(r'rooms', room_view.RoomViewSet)
router.register(r'sensors', sensor_view.SensorViewSet)
router.register(r'sensor_results', sensor_result_view.SensorResultViewSet)
router.register(r'room_occupancy', room_occupancy_view.RoomOccupancyViewSet)


# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),

]
