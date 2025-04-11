from django.db import models


class Locations(models.TextChoices):
    WINDOW_HALL = 'window hall', 'Зал у окна'
    MAIN_HALL = 'main hall', 'Основной зал'
    TERRACE = 'terrace', 'Терраса'


class Table(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название стола")
    seats = models.IntegerField(verbose_name="Количество мест")
    location = models.CharField(
        max_length=50, 
        choices=Locations.choices, 
        default=Locations.MAIN_HALL, 
        verbose_name="Расположение стола"
        )

    def __str__(self):
        return f"{self.name} ({self.location})"


class Reservation(models.Model):
    customer_name = models.CharField(max_length=100, verbose_name="Имя посетителя")
    table = models.ForeignKey(
        Table, 
        on_delete=models.CASCADE, 
        related_name="reservations", 
        verbose_name="Номер стола")
    reservation_time = models.DateTimeField(verbose_name="Время брони")
    duration_minutes = models.IntegerField(verbose_name="Длительность брони")

    def __str__(self):
        return f"{self.customer_name} - {self.table.name} - {self.reservation_time}"