from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class CustomUse(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.email



class Booking(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='bookingsCollection')
    title = models.CharField(max_length=300)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.FloatField()
    hours = models.IntegerField()

    def __str__(self):
        return self.title



class Account(models.Model):
    name = models.CharField(max_length=200)
    company_ID = models.OneToOneField(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


