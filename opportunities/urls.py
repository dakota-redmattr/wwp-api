from django.contrib import admin
from django.urls import path, include
from .views import PositionAPIView, PositionListingDetailAPIView

urlpatterns = [
    path('', PositionAPIView.as_view(), name='positions'),
    path('<int:id>/',
         PositionListingDetailAPIView.as_view(), name="position-detail")
]
