from django.contrib import admin
from .models import FoodCategory, FoodItem, DrinkCategory, DrinkItem

# Register your models here.
admin.site.register(FoodCategory)
admin.site.register(FoodItem)
admin.site.register(DrinkCategory)
admin.site.register(DrinkItem)
