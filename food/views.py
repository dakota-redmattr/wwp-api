from django.shortcuts import render
from .models import FoodCategory, FoodItem, DrinkCategory, DrinkItem
from rest_framework.generics import ListAPIView
from .serializers import FoodCategorySerializer, FoodCategoryDetailSerializer, FoodItemSerializer, DrinkCategorySerializer, DrinkItemSerializer


class DrinkCategoryAPIView(ListAPIView):
    queryset = DrinkCategory.objects.all()
    serializer_class = DrinkCategorySerializer


class FoodCategoryAPIView(ListAPIView):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodCategorySerializer


class FoodCategoryDetailAPIView(ListAPIView):
    serializer_class = FoodCategorySerializer

    def get_queryset(self):
        return FoodCategory.objects.filter(slug=self.kwargs['slug'])
