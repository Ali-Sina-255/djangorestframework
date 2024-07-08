from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token


class Flight(models.Model):
    flight_number = models.CharField(max_length=255)
    operating_api_lines = models.CharField(max_length=255)
    departure_city = models.CharField(max_length=100)
    arrive_city = models.CharField(max_length=190)
    date_of_departure = models.DateField()
    estimated_time_of_departure = models.TimeField()

    def __str__(self):
        return self.flight_number


class Passenger(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email_address = models.EmailField(unique=True, max_length=200)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.first_name


class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def createAuthToken(sender, created, instance, **kwargs):
    if created:
        Token.objects.create(user=instance)
