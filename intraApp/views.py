from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UserSerializer, SecondaryEmailsSerializer, CompanySerializer
from .models import User, Company
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.


# class SecondaryEmailsListAPIView(ListCreateAPIView):
#     serializer_class = SecondaryEmailsSerializer
#     queryset = User.objects.all()


# class SecondaryEmailsDetailAPIView(RetrieveUpdateDestroyAPIView):
#     serializer_class = SecondaryEmailsSerializer
#     queryset = User.objects.all()
#     lookup_field = "id"



class UserListAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "id"



class CompanyListAPIView(ListCreateAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class CompanyDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    lookup_field = "id"



# class LoginAPIView(generics.GenericAPIView):
#     serializer_class = LoginSerializer

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


