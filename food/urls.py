from django.contrib import admin
from django.urls import path, include
from .views import FoodCategoryAPIView, FoodCategoryDetailAPIView

urlpatterns = [
    path('', FoodCategoryAPIView.as_view(), name='food'),
    path('<slug:slug>/',
         FoodCategoryDetailAPIView.as_view(), name="food-detail")
]
