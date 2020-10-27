from django.shortcuts import render
from .models import Location, LocationHours
from rest_framework.generics import ListAPIView
from .serializers import LocationSerializer


class LocationAPIView(ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
