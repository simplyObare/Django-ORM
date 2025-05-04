from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Restaurant
# Ratings
# User


class Restaurant(models.Model):
    class TypeChoices(models.TextChoices):
        INDIAN = "IN", "Indian"
        CHINESE = "CH", "Chinese"
        ITALIAN = "IT", "Italian"
        GREEK = "GR", "Greek"
        FASTFOOD = "FF", "Fast Food"
        OTHER = "OT", "Others"

    name = models.CharField(max_length=100)
    website = models.URLField(default="", blank=True, null=True)
    date_opened = models.DateField()
    latitude = models.FloatField(
        validators=[MinValueValidator(-90), MaxValueValidator(90)]
    )
    longitude = models.FloatField(
        validators=[MinValueValidator(-180), MaxValueValidator(180)]
    )
    restaurant_type = models.CharField(max_length=2, choices=TypeChoices.choices)

    def __str__(self):
        return f"Name of Restaurant: {self.name} Type of Restaurant: {self.restaurant_type}"

    def save(self, *args, **kwargs):
        print(self._state.adding)
        super().save(*args, **kwargs)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="ratings"
    )
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return f"{self.user.username} - {self.restaurant.name} - {self.rating}"


class Sale(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.SET_NULL, null=True, related_name="sales"
    )
    income = models.DecimalField(max_digits=10, decimal_places=2)
    datetime = models.DateTimeField()
