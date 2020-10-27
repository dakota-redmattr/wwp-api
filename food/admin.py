from django.contrib import admin
from .models import FoodCategory, FoodItem

# Register your models here.
admin.site.register(FoodCategory)
admin.site.register(FoodItem)
