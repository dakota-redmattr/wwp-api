from rest_framework import serializers
from locations.serializers import LocationSerializer
from .models import PositionListing, PositionType


class PositionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PositionType
        fields = ['name', 'description']


class PositionListingSerializer(serializers.ModelSerializer):
    position = PositionTypeSerializer()
    location = LocationSerializer()

    class Meta:
        model = PositionListing
        fields = ["id", "position", "location", "post_date"]


class PositionListingDetailSerializer(serializers.ModelSerializer):
    position = PositionTypeSerializer()
    location = LocationSerializer()

    class Meta:
        model = PositionListing
        fields = ['url', "id", "position", "location", "post_date"]
        lookup_field = 'id'
        extra_kwargs = {
            'url': {'lookup_field': 'id'}
        }
