from django.db import models
from locations.models import Location


class PositionType(models.Model):
    name = models.CharField(max_length=150, null=False)
    description = models.TextField(null=False)

    def __str__(self):
        return self.name


class PositionListing(models.Model):
    position = models.ForeignKey(
        PositionType, on_delete=models.CASCADE, related_name="position")
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name="location")
    post_date = models.DateTimeField(auto_now_add=True)
    filled = models.BooleanField(default=False)

    def __str__(self):
        return self.location.name + " - " + self.position.name
