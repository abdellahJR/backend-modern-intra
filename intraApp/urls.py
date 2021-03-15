from django.urls import path
from .views import CustomUserListAPIView, CustomUserDetailAPIView, CompanyListAPIView, CompanyDetailAPIView

urlpatterns = [
    path('users/', CustomUserListAPIView.as_view(), name="list-user"),
    path('users/<int:id>/', CustomUserDetailAPIView.as_view(), name="detail-user"),
    path('company/', CompanyListAPIView.as_view(), name="list-company"),
    path('company/<int:id>/', CompanyDetailAPIView.as_view(), name="detail-company"),
]



