from rest_framework import serializers
from .models import Invoice

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', "billFromAddress", "fromCity","fromPostCode","fromCountry",
                  "clientName", "clientEmail","clientStreetAddress",
                  "toCity", "toPostCode", "toCountry", "invoiceDate", 
                  "paymentTerms", "projectDescription", "invoiceStatus", "markAsPaid",
                  "items"]
