from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_api_view),
    path('', views.category_api_view),
    path("/categories/<int: id>/", views.category_detail_api_view)
]
