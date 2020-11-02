from django.db import models


class FoodCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    slug = models.SlugField()
    order_index = models.IntegerField(null=True)

    class Meta:
        verbose_name = "Food Category"
        verbose_name_plural = "Food Categories"

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    name = models.CharField(max_length=150, null=False)
    description = models.TextField(null=False)
    price = models.FloatField(null=True)
    category = models.ForeignKey(
        FoodCategory, related_name="items", on_delete=models.CASCADE)
    order_index = models.IntegerField(null=True)

    class Meta:
        verbose_name = "Food Item"
        verbose_name_plural = "Food Items"

    def __str__(self):
        return self.name


class DrinkCategory(models.Model):
    name = models.CharField(max_length=150, null=False)
    description = models.TextField(null=True, blank=True)
    listed = models.BooleanField()
    order_index = models.IntegerField(null=True)

    class Meta:
        verbose_name = "Drink Category"
        verbose_name_plural = "Drink Categories"

    def __str__(self):
        return self.name


class DrinkItem(models.Model):
    name = models.CharField(max_length=180, null=False)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True)
    category = models.ForeignKey(
        DrinkCategory, related_name="items", on_delete=models.CASCADE)
    order_index = models.IntegerField(null=True)

    class Meta:
        verbose_name = "Drink Item"
        verbose_name_plural = "Drink Items"

    def __str__(self):
        return self.name
