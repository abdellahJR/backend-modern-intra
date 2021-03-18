
from rest_framework import serializers
from .models import User, Company, SecondaryEmails
from rest_framework_simplejwt.tokens import RefreshToken


class SecondaryEmailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondaryEmails
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    secondaryEmails = serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    user_id = UserSerializer(many=True)
    class Meta:
        model = Company
        fields ='__all__'


# class LoginSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(max_length=255, min_length=3)
#     password = serializers.CharField(
#         max_length=68, min_length=6, write_only=True)

#     tokens = serializers.SerializerMethodField(read_only=True)

#     def get_tokens(self, obj):
#         user = User.objects.get(email=obj['email'])

#         return {
#             'refresh': user.tokens()['refresh'],
#             'access': user.tokens()['access']
#         }

#     class Meta:
#         model = User
#         fields = ['email', 'password', 'tokens']

#     def validate(self, attrs):
#         email = attrs.get('email', '')
#         password = attrs.get('password', '')
#         filtered_user_by_email = User.objects.filter(email=email)
#         user = auth.authenticate(email=email, password=password)

#         if not user:
#             raise AuthenticationFailed('Invalid credentials, try again')

#         return {
#             'email': user.email,
#             'tokens': user.tokens
#         }

#         return super().validate(attrs)


# class LogoutSerializer(serializers.Serializer):
#     refresh = serializers.CharField()

#     default_error_message = {
#         'bad_token': 'Token is expired or invalid'
#     }

#     def validate(self, attrs):
#         self.token = attrs['refresh']
#         return attrs

#     def save(self, **kwargs):

#         try:
#             RefreshToken(self.token).blacklist()

#         except TokenError:
#             self.fail('bad_token')