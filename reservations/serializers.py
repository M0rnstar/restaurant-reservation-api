from rest_framework import serializers
from .models import Table, Reservation
from django.utils import timezone
from datetime import timedelta

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"

    def validate(self, data):
        table = data['table']
        start_time = data['reservation_time']
        duration = data['duration_minutes']
        end_time = start_time + timedelta(minutes=duration)

        reservations = Reservation.objects.filter(table=table)

        if self.instance:
            reservations = reservations.exclude(id=self.instance.id)

        for res in reservations:
            res_start = res.reservation_time
            res_end = res_start + timedelta(minutes=res.duration_minutes)

            if start_time < res_end and end_time > res_start:
                raise serializers.ValidationError("Этот стол уже забронирован на выбранное время.")

        return data