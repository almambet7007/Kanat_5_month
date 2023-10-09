from rest_framework import serializers
from .models import Product, Review, Category


class ProductSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = '__all__'


class ReviewSerializer(serializers.Serializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProductReviewSerializer(serializers.Serializer):
    review = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
