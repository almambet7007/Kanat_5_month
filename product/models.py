from django.db import models
from django.core import validators


class Category(models.Model):
    name = models.CharField(max_length=255)

    def product_count(self):
        return self.product_set.count()

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    starts = models.IntegerField(validators=[validators.MinValueValidator(1), validators.MaxValueValidator(5)])

    def __str__(self):
        return self.text
