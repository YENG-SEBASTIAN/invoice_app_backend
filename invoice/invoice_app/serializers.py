from rest_framework import serializers
from django.db import models
from .models import Invoice, Item

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', "billFromAddress", "fromCity","fromPostCode","fromCountry",
                  "clientName", "clientEmail","clientStreetAddress",
                  "toCity", "toPostCode", "toCountry", "invoiceDate", 
                  "paymentTerms", "projectDescription", "invoiceStatus", "markAsPaid",
                  "items"]
        
        
class InvoiceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', "createdAt ", "paymentDue ","description ","paymentTerms ",
                  "clientName ", "clientEmail ","status ",
                  "sendersAddress ", "clientAddress ", "items ", "total"]
        
class Filter(serializers.Serializer):
    filterName = serializers.CharField()
                