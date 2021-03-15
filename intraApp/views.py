from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CustomUserSerializer, SecondaryEmailsSerializer, CompanySerializer
from .models import CustomUser, Company
# Create your views here.


# class SecondaryEmailsListAPIView(ListCreateAPIView):
#     serializer_class = SecondaryEmailsSerializer
#     queryset = User.objects.all()


# class SecondaryEmailsDetailAPIView(RetrieveUpdateDestroyAPIView):
#     serializer_class = SecondaryEmailsSerializer
#     queryset = User.objects.all()
#     lookup_field = "id"



class CustomUserListAPIView(ListCreateAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()


class CustomUserDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    lookup_field = "id"



class CompanyListAPIView(ListCreateAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class CompanyDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    lookup_field = "id"