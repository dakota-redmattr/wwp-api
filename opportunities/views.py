from django.shortcuts import render
from .models import PositionType, PositionListing
from rest_framework.generics import ListAPIView
from locations.serializers import LocationSerializer
from .serializers import PositionListingSerializer, PositionTypeSerializer, PositionListingDetailSerializer


class PositionAPIView(ListAPIView):
    queryset = PositionListing.objects.all()
    serializer_class = PositionListingSerializer

class PositionListingDetailAPIView(ListAPIView):
    serializer_class = PositionListingSerializer

    def get_queryset(self):
        return PositionListing.objects.filter(id=self.kwargs['id'])
