from django.contrib import admin
from django.urls import path, include
from .views import LocationAPIView

urlpatterns = [
    path('', LocationAPIView.as_view(), name='food'),
]
