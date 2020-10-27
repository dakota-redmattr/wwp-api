from django import forms
from django.db import models
from django.core.validators import RegexValidator


class Location(models.Model):
    name = models.CharField(max_length=150, null=False)
    street_address_1 = models.CharField(max_length=150, null=False)
    street_address_2 = models.CharField(max_length=150, null=True)
    city = models.CharField(max_length=150, null=False)
    state = models.CharField(max_length=2, null=False)
    zip_code = models.IntegerField(null=False)
    image = models.ImageField()
    slug = models.SlugField()
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # validators should be a list
    phone = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)

    def __str__(self):
        return self.name


class LocationHours(models.Model):
    monday_open = models.TimeField()
    monday_close = models.TimeField()
    tuesday_open = models.TimeField()
    tuesday_close = models.TimeField()
    wednesday_open = models.TimeField()
    wednesday_close = models.TimeField()
    thursday_open = models.TimeField()
    thursday_close = models.TimeField()
    friday_open = models.TimeField()
    friday_close = models.TimeField()
    saturday_open = models.TimeField()
    saturday_close = models.TimeField()
    sunday_open = models.TimeField()
    sunday_close = models.TimeField()
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name="hours")

    class Meta:
        verbose_name = "Location Hours"
        verbose_name_plural = "Location Hours"

    def __str__(self):
        return self.location.name
