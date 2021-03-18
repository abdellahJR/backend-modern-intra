from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class SecondaryEmails(models.Model):
    email = models.EmailField(blank=True, null=True, unique=True)

    def __str__(self):
        return self.email


class UserManager(BaseUserManager):

    def create_user(self, email, password, **other_fields):

        if email is None:
            raise TypeError('Users should have a email')

        user = self.model(email=self.normalize_email(
            email), **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(email, password, **other_fields)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):

    USER_TYPE = [
        ('client', 'client'),
        ('employee', 'employee'),
    ]

    email = models.EmailField(max_length=225, unique=True, db_index=True)
    first_name = models.CharField(max_length=25, blank=True)
    last_name = models.CharField(max_length=25, blank=True)
    user_type = models.CharField(choices=USER_TYPE, default='client', max_length=8, blank=True, null=True)
    secondaryEmails = models.ManyToManyField(SecondaryEmails, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }




class Company(models.Model):
    name = models.CharField(max_length=200, unique=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='bookingsCollection')
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.company



class Account(models.Model):
    name = models.CharField(max_length=200)
    company_id = models.OneToOneField(Company, on_delete=models.CASCADE)

    def get_company_customer(self):
        return self.company_id.user_id

    def get_company_partner(self):
        return self.company_id

    def __str__(self):
        return self.name


