from django.contrib import admin
from .models import LocationHours, Location


class InLineHours(admin.StackedInline):
    model = LocationHours
    extra = 1
    max_num = 1
    fields = (
        ("monday_open", "monday_close"),
        ("tuesday_open", "tuesday_close"),
        ("wednesday_open", "wednesday_close"),
        ("thursday_open", "thursday_close"),
        ("friday_open", "friday_close"),
        ("saturday_open", "saturday_close"),
        ("sunday_open", "sunday_close"),
    )


class LocationAdmin(admin.ModelAdmin):
    inlines = [InLineHours]
    fields = (
        'name',
        'street_address_1',
        'street_address_2',
        'city',
        'state',
        'zip_code',
        'image',
        'slug',
        'phone',
    )


# Register your models here.
admin.site.register(Location, LocationAdmin)
