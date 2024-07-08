import re

from rest_framework import serializers
from flightApp.models import Passenger, Flight, Reservation


class FlightSerializers(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

    def validate(self, attrs):
        print("the validated data function is called")
        return attrs


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
