from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)



urlpatterns = [
    path('users/', UserListAPIView.as_view(), name="list-user"),
    path('users/<int:id>/', UserDetailAPIView.as_view(), name="detail-user"),
    path('company/', CompanyListAPIView.as_view(), name="list-company"),
    path('company/<int:id>/', CompanyDetailAPIView.as_view(), name="detail-company"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]



