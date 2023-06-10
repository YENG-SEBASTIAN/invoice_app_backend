from django.db import models
from django.contrib.postgres.fields import ArrayField
# from django_mysql.models import ListCharField


# Create your models here.
class Invoice(models.Model):
    #bill form
    streetAddress = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postCode = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    #Bill to
    clientName = models.CharField(max_length=100)
    clientEmail = models.EmailField(max_length=100)
    clientStreetAddress = models.CharField(max_length=100)
    clientCity = models.CharField(max_length=100)
    clientPostCode = models.CharField(max_length=100)
    clientCountry = models.CharField(max_length=100)
    invoiceDate = models.DateField(auto_now_add=True)
    paymentTerms = models.CharField(max_length=100)
    projectDescription = models.CharField(max_length=200)
    invoiceStatus = models.CharField(max_length=100, blank=True)
    markAsPaid = models.BooleanField(default=False)
    #items
    itemName = ArrayField(
            models.CharField(max_length=10, blank=True),
            size=20,
    )
    itemQuantity = ArrayField(models.IntegerField())
    itemPrice = ArrayField(models.IntegerField())
    totalPrice = ArrayField(models.IntegerField())
    
    def __str__(self):
        return self.clientName
    