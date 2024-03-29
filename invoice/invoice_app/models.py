from django.db import models
//array field
from django.contrib.postgres.fields import ArrayField, JSONField


# Create your models here.
class Invoice(models.Model):
    #bill form
    billFromAddress = models.CharField(max_length=100)
    fromCity = models.CharField(max_length=100)
    fromPostCode = models.CharField(max_length=100)
    fromCountry = models.CharField(max_length=100)
    #Bill to
    clientName = models.CharField(max_length=100)
    clientEmail = models.EmailField(max_length=100)
    clientStreetAddress = models.CharField(max_length=100)
    toCity = models.CharField(max_length=100)
    toPostCode = models.CharField(max_length=100)
    toCountry = models.CharField(max_length=100)
    invoiceDate = models.DateField(auto_now_add=True)
    paymentTerms = models.CharField(max_length=100, blank=True)
    projectDescription = models.CharField(max_length=200)
    invoiceStatus = models.CharField(max_length=100, blank=True)
    markAsPaid = models.BooleanField(default=False)
    #items
    items = models.JSONField()

    
    
    def __str__(self):  
        return self.clientName
