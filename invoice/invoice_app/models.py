from django.db import models

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
    #items
    itemName = models.CharField(max_length=100)
    itemQuantity = models.CharField(max_length=100)
    itemPrice = models.IntegerField()
    totalPrice = models.IntegerField()
    
    def __str__(self):
        return self.clientName