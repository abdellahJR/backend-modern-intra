from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=200)
    user_id = models.ForeignKey(CustomUse, on_delete=models.CASCADE, null=true)

    def __str__(self):
        return self.name


class CustomUse(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

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


