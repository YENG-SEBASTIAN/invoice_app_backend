from rest_framework import serializers

from .models import Invoice, Item

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', "streetAddress", "city","postCode","country",
                  "clientName", "clientEmail","clientStreetAddress",
                  "clientCity", "clientPostCode", "clientCountry", 
                  "invoiceDate", "paymentTerms", "projectDescription"]
        

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["item", "itemName", "itemQuantity", "itemPrice", "totalPrice"]