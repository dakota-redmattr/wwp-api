from rest_framework import serializers
from .models import Location, LocationHours


class LocationHourSerializer(serializers.ModelSerializer):
    monday_open = serializers.TimeField(
        format='%-I:%M %p', input_formats='%-I:%M %p')
    monday_close = serializers.TimeField(
        format='%-I:%M %p', input_formats='%-I:%M %p')
    tuesday_open = serializers.TimeField(
        format='%-I:%M %p', input_formats='%-I:%M %p')
    tuesday_close = serializers.TimeField(
        format='%-I:%M %p', input_formats='%-I:%M %p')
    wednesday_open = serializers.TimeField(
        format='%-I:%M %p', input_formats='%-I:%M %p')
    wednesday_close = serializers.TimeField(
        format='%-I:%M %p', input_formats='%-I:%M %p')
    thursday_open = serializers.TimeField(
        format='%-I:%M %p', input_formats='%-I:%M %p')
    thursday_close = serializers.TimeField(
        format='%-I:%M %p', input_formats='%-I:%M %p')
    friday_open = serializers.TimeField(
        format='%-I:%M %p', input_formats='%-I:%M %p')
    friday_close = serializers.TimeField(
        format='%-I:%M %p', input_formats='%-I:%M %p')
    saturday_open = serializers.TimeField(
        format='%-I:%M %p', input_formats='%-I:%M %p')
    saturday_close = serializers.TimeField(
        format='%-I:%M %p', input_formats='%-I:%M %p')
    sunday_open = serializers.TimeField(
        format='%-I:%M %p', input_formats='%-I:%M %p')
    sunday_close = serializers.TimeField(
        format='%-I:%M %p', input_formats='%-I:%M %p')

    class Meta:
        model = LocationHours
        fields = ['monday_open', 'monday_close', 'tuesday_open', 'tuesday_close', 'wednesday_open', 'wednesday_close', 'thursday_open',
                  'thursday_close', 'friday_open', 'friday_close', 'saturday_open', 'saturday_close', 'sunday_open', 'sunday_close']


class LocationSerializer(serializers.ModelSerializer):
    hours = LocationHourSerializer(many=True, read_only=True)

    class Meta:
        model = Location
        fields = ['name', 'street_address_1', 'street_address_2',
                  'city', 'state', 'zip_code', 'image', 'slug', 'phone', 'hours']
