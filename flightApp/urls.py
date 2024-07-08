from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('flights', views.FlightListApiViewSet)
router.register('passenger', views.PassengerApiViewSet)
router.register('reservation', views.ReservationApiViewSet)
urlpatterns = [
    path("flightServices/", include(router.urls)),
    path('flightServices/saveReservation/', views.ReservationFlights.as_view()),
    path('api-auth-token/', obtain_auth_token, name='auth-token'),
]
