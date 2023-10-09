from rest_framework import serializers
from .models import Product, Review, Category


class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, required=True)
    description = serializers.CharField(max_length=255, required=True)
    price = serializers.IntegerField(min_value=1, required=True)
    category = serializers.IntegerField(required=True)

    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, required=True)

    class Meta:
        model = Category
        fields = '__all__'


class ReviewSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=255, required=False)
    product = serializers.IntegerField(required=True)
    stars = serializers.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = Review
        fields = '__all__'


class ProductReviewSerializer(serializers.Serializer):
    review = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
