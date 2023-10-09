from django.urls import path
from .views import (
    CategoryAPIView,
    CategoryDetailAPIView,
    ProductAPIView,
    ProductDetailAPIView,
    ReviewAPIView,
    ReviewDetailAPIView,
    ProductReviewAPIView,
)

urlpatterns = [
    path('categories/', CategoryAPIView.as_view(), name='category-list'),
    path('categories/<int:id>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('products/', ProductAPIView.as_view(), name='product-list'),
    path('products/<int:id>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('reviews/', ReviewAPIView.as_view(), name='review-list'),
    path('reviews/<int:id>/', ReviewDetailAPIView.as_view(), name='review-detail'),
    path('products/reviews/', ProductReviewAPIView.as_view(), name='product-review-list'),
]
