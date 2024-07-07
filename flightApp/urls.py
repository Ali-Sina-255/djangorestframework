from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('flights', views.FlightListApiViewSet)
router.register('passenger', views.PassengerApiViewSet)
router.register('reservation', views.ReservationApiViewSet)
urlpatterns = [
    path("flightServices/", include(router.urls))

]
