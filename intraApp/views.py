from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CustomUseSerializer, SecondaryEmailsSerializer, CompanySerializer
from .models import CustomUse, Company
# Create your views here.


# class SecondaryEmailsListAPIView(ListCreateAPIView):
#     serializer_class = SecondaryEmailsSerializer
#     queryset = User.objects.all()


# class SecondaryEmailsDetailAPIView(RetrieveUpdateDestroyAPIView):
#     serializer_class = SecondaryEmailsSerializer
#     queryset = User.objects.all()
#     lookup_field = "id"



class CustomUseListAPIView(ListCreateAPIView):
    serializer_class = CustomUseSerializer
    queryset = CustomUse.objects.all()


class CustomUseDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CustomUseSerializer
    queryset = CustomUse.objects.all()
    lookup_field = "id"



class CompanyListAPIView(ListCreateAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class CompanyDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    lookup_field = "id"