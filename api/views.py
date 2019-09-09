from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from api.models import Flight, Plane, Ticket
from api.serializers import FlightSerializer, PlaneSerializer, TicketSerializer, UserSerializer
from api.permissions import IsAdminOrReadOnly


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsAdminOrReadOnly]


class PlaneViewSet(viewsets.ModelViewSet):
    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer
    permission_classes = [IsAdminOrReadOnly]


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
