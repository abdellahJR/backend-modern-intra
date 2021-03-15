
from rest_framework import serializers
from .models import CustomUser, Company, SecondaryEmails


class SecondaryEmailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondaryEmails
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    secondaryEmails = serializers.StringRelatedField(many=True)
    class Meta:
        model = CustomUser
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    user_id = CustomUserSerializer(many=True)
    class Meta:
        model = Company
        fields ='__all__'