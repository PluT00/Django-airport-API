from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify


class Flight(models.Model):
    STATUS_CHOISES = (
        ('Registration', 'Registration'),
        ('On the way', 'On the way'),
        ('Delayed', 'Delayed'),
        ('Canceled', 'Canceled'),
        ('Arrived', 'Arrived'),
        ('Departure', 'Departure')
    )
    departure_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    flight_id = models.CharField(max_length=10, unique=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    arrival_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    company = models.CharField(max_length=50)
    plane_name = models.ForeignKey(
        'Plane',
        on_delete=models.CASCADE,
    )
    status = models.CharField(
        max_length=12,
        choices=STATUS_CHOISES,
        default='Registration'
    )
    is_departure = models.BooleanField(default=True)
    slug = models.SlugField(max_length=10, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.flight_id)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.flight_id

    class Meta:
        ordering = ['-departure_time']


class Plane(models.Model):
    name = models.CharField(max_length=20)
    seats = models.IntegerField(default=120)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    user = models.ForeignKey(User, related_name="tickets", on_delete=models.CASCADE)
    flight = models.ForeignKey('Flight', on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.user.username, self.flight.flight_id)
