from django.urls import path
from .views import RegistrationUserAPIView, ConfirmUserAPIView, LoginUserAPIView

urlpatterns = [
    path('register/', RegistrationUserAPIView.as_view(), name='register'),
    path('confirm/', ConfirmUserAPIView.as_view(), name='confirm'),
    path('login/', LoginUserAPIView.as_view(), name='login'),
]
