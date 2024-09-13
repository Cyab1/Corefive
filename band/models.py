from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    """
    Represents a band member.

    Attributes:
        name (str): The name of the band member.
        instrument (str): The instrument played by the member.
        bio (str): A brief biography of the member.
        image (ImageField): An optional image of the member.
    """

    name = models.CharField(max_length=100)
    instrument = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to="members/", blank=True, null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    """
    Represents a band event or concert.

    Attributes:
        name (str): The name of the event.
        date (Date): The date of the event.
        description (str): A description of the event.
        price (Decimal): The price of tickets for the event.
    """

    name = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.event.name} - {self.quantity} tickets"
