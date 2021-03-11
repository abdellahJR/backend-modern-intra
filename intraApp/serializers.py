
from rest_framework import serializers
from .models import CustomUse, Company, SecondaryEmails


class SecondaryEmailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondaryEmails
        fields = '__all__'





class CustomUseSerializer(serializers.ModelSerializer):
    secondaryEmails = SecondaryEmailsSerializer(many=True)

    class Meta:
        model = CustomUse
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    user_id = CustomUseSerializer()
    class Meta:
        model = Company
        fields ='__all__'