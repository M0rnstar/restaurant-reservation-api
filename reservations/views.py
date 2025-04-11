from rest_framework import viewsets, mixins
from .models import Table, Reservation
from .serializers import TableSerializer, ReservationSerializer


class TableViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class ReservationViewSet(mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer