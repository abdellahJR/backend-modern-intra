from django.db import models

# Create your models here.



class SecondaryEmails(models.Model):
    email = models.EmailField(blank=True, null=True, unique=True)

    def __str__(self):
        return self.email


class CustomUser(models.Model):

    USER_TYPE = [
        ('client', 'client'),
        ('employee', 'employee'),
    ]

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    user_type = models.CharField(choices=USER_TYPE, max_length=8, blank=True, null=True)
    secondaryEmails = models.ManyToManyField(SecondaryEmails, blank=True)
    hourlyRate = models.PositiveIntegerField(blank=True, null=True)

    @property
    def is_client(self):
        if self.user_type == 'client':
            return True

    def __str__(self):
        return self.first_name


class Company(models.Model):
    name = models.CharField(max_length=200, unique=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)

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


