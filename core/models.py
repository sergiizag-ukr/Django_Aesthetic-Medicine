from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    phone = models.CharField(max_length=20)

    email = models.EmailField()

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    SKIN_TYPES = [
        ("oily", "Жирна"),
        ("dry", "Суха"),
        ("combination", "Комбінована"),
        ("sensitive", "Чутлива"),
    ]

    skin_type = models.CharField(
        max_length=20,
        choices=SKIN_TYPES,
        blank=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Service(models.Model):
    name = models.CharField(max_length=100)

    description = models.TextField(
        blank=True
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    duration_hours = models.FloatField(
        default=1
    )

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = [
        ("new", "Новий"),
        ("in_progress", "У процесі"),
        ("completed", "Готово"),
        ("cancelled", "Скасовано"),
    ]

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE
    )

    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new"
    )

    date = models.DateField(
        null=True,
        blank=True
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    completed_at = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Order #{self.id}"


class Inventory(models.Model):
    name = models.CharField(max_length=100)

    description = models.TextField(
        blank=True
    )

    quantity = models.IntegerField()

    min_quantity = models.IntegerField(
        default=5
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    category = models.CharField(
        max_length=100,
        blank=True
    )

    def __str__(self):
        return self.name

class PatientProfile(models.Model):
    client = models.OneToOneField(
        Client,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    allergies = models.TextField(
        blank=True
    )

    previous_treatments = models.TextField(
        blank=True
    )

    preferred_procedures = models.CharField(
        max_length=200,
        blank=True
    )

    def __str__(self):
        return f"Профіль {self.client}"