from django.urls import path
from .views import CustomUseListAPIView, CustomUseDetailAPIView, CompanyListAPIView, CompanyDetailAPIView

urlpatterns = [
    path('users/', CustomUseListAPIView.as_view(), name="list-users"),
    path('users/<int:id>/', CustomUseDetailAPIView.as_view(), name="detail-user"),
    path('company/', CompanyListAPIView.as_view(), name="list-company"),
    path('company/<int:id>/', CompanyDetailAPIView.as_view(), name="detail-company"),
]

