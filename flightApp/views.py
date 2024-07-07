from django.shortcuts import render
from .models import Flight, Reservation, Passenger
from .serializers import FlightSerializers, PassengerSerializer, ReservationSerializer
from rest_framework import viewsets


class FlightListApiViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializers


class PassengerApiViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class ReservationApiViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
