import pytest
from django.utils import timezone
from datetime import timedelta
from reservations.models import Table
from reservations.serializers import TableSerializer, ReservationSerializer


# Проверка успешного создания стола
@pytest.mark.django_db
def test_create_table_success():
    data = {
        "name": "Table 1",
        "seats": 2,
        "location": "terrace"
    }
    serializer = TableSerializer(data=data)
    assert serializer.is_valid(), serializer.errors
    table = serializer.save()
    assert table.name == "Table 1"
    assert table.location == "terrace"


# Проверка успешного создания брони
@pytest.mark.django_db
def test_create_reservation_success():
    table = Table.objects.create(
        name="Table 1", 
        seats=2, 
        location="window hall"
        )

    start_time = timezone.now() + timedelta(hours=1)

    serializer = ReservationSerializer(data={
        "customer_name": "Тестовый клиент",
        "table": table.id,
        "reservation_time": start_time,
        "duration_minutes": 90
    })

    assert serializer.is_valid(), serializer.errors
    reservation = serializer.save()
    assert reservation.id is not None
    assert reservation.customer_name == "Тестовый клиент"


# Проверка конфликтов брони
@pytest.mark.django_db
def test_create_reservation_conflict():
    table = Table.objects.create(
        name="Table 2", 
        seats=4, 
        location="terrace"
        )

    start_time = timezone.now() + timedelta(hours=2)

    # Первая бронь
    serializer1 = ReservationSerializer(data={
        "customer_name": "Первый клиент",
        "table": table.id,
        "reservation_time": start_time,
        "duration_minutes": 60
    })
    assert serializer1.is_valid(), serializer1.errors
    serializer1.save()

    # Вторая бронь(начинается через 30 минут)
    serializer2 = ReservationSerializer(data={
        "customer_name": "Второе клиент",
        "table": table.id,
        "reservation_time": start_time + timedelta(minutes=30),
        "duration_minutes": 60
    })
    assert not serializer2.is_valid(), "Ожидалась ошибка валидации, но её нет"
    assert "non_field_errors" in serializer2.errors