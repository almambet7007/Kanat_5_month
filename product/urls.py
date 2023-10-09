from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_api_view),
    path('categories/<int:id>/', views.category_detail_api_view),
    path('products', views.product_api_view),
    path('products/<int:id>', views.product_detail_api_view),
    path('reviews', views.review_api_view),
    path('reviews/<int:id>', views.review_detail_api_view),
    path('products/reviews/', views.product_review_api_view)
]

