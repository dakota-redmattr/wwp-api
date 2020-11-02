from django.contrib import admin
from django.urls import path, include
from .views import FoodCategoryAPIView, FoodCategoryDetailAPIView, DrinkCategoryAPIView

urlpatterns = [
    path('', FoodCategoryAPIView.as_view(), name='food'),
    path('drinks/', DrinkCategoryAPIView.as_view(), name='drinks'),
    path('<slug:slug>/',
         FoodCategoryDetailAPIView.as_view(), name="food-detail")
]
