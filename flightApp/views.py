from django.shortcuts import render
from .models import Flight, Reservation, Passenger
from .serializers import FlightSerializers, PassengerSerializer, ReservationSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Flight, Passenger, Reservation
from .serializers import PassengerSerializer, ReservationSerializer
from rest_framework.permissions import IsAuthenticated


class ReservationFlights(APIView):
    def post(self, request, *args, **kwargs):
        flight_id = request.data.get('flightId')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email_address = request.data.get('email_address')
        phone_number = request.data.get('phone_number')

        try:
            flight = Flight.objects.get(id=flight_id)
        except Flight.DoesNotExist:
            return Response({'error': 'Flight not found'}, status=status.HTTP_404_NOT_FOUND)

        passenger_data = {
            'first_name': first_name,
            'last_name': last_name,
            'email_address': email_address,
            'phone_number': phone_number
        }

        passenger_serializer = PassengerSerializer(data=passenger_data)
        if passenger_serializer.is_valid():
            passenger = passenger_serializer.save()
        else:
            return Response(passenger_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        reservation = Reservation(flight=flight, passenger=passenger)
        reservation.save()

        return Response({'message': 'Reservation created successfully'}, status=status.HTTP_201_CREATED)


# def reservation_flights(request):
#     flights = Flight.objects.get(id=request.data['flightId'])
#     passenger = Passenger()
#     passenger.first_name = request.data['first_name']
#     passenger.last_name = request.data['last_name']
#     passenger.email_address = request.data["email_address"]
#     passenger.phone_number = request.data["phone_number"]
#     reservation = Reservation()
#     reservation.flight = flights
#     reservation.passenger = passenger
#     Reservation.save(reservation)
#     return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
def find_flights(request):
    fligths = Flight.objects.filter(departure_city=request.data['departure_city'], arrive_city=request.data[
        'arrive_city'], date_of_departure=request.data['date_of_departure'])
    serializer = FlightSerializers(fligths, many=True)
    return Response(serializer.data)


class FlightListApiViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializers
    permission_classes = (IsAuthenticated,)


class PassengerApiViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class ReservationApiViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
