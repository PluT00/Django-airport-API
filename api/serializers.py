from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Flight, Plane, Ticket


class FlightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Flight
        fields = ['url', 'id', 'departure_time', 'flight_id', 'country', 'city',
                  'arrival_time', 'company', 'plane_name', 'status',
                  'is_departure']


class PlaneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plane
        fields = ['url', 'id', 'name', 'seats']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    tickets = serializers.HyperlinkedRelatedField(many=True,
                                                  view_name='ticket-detail',
                                                  read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'tickets']


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Ticket
        fields = ['url', 'id', 'user', 'flight']
