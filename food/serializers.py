from rest_framework import serializers
from .models import FoodCategory, FoodItem


# Food Item Serializer


class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ['id', 'name', 'description', 'price', 'order_index']


# Food Category Serializer


class FoodCategorySerializer(serializers.ModelSerializer):
    items = FoodItemSerializer(many=True, read_only=True)

    class Meta:
        model = FoodCategory
        fields = ['name', 'image', 'slug', 'order_index', 'items']


# Food Category Serializer


class FoodCategoryDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodCategory
        fields = ['url', 'id', 'slug', 'name']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
