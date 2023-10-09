from django.core.exceptions import ValidationError
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
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField('Tag')
    def __str__(self):
        return self.title

    def clean(self):
        # Переопределяем метод clean для валидации тэгов
        super().clean()
        for tag in self.tags.all():
            if not Tag.objects.filter(name=tag.name).exists():
                raise ValidationError(f"Тэг '{tag.name}' не существует в базе данных. Укажите существующие тэги.")

class Review(models.Model):
    text = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[validators.MinValueValidator(1), validators.MaxValueValidator(5)])

    def __str__(self):
        return self.text


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

