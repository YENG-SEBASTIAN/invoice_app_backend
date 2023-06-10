from rest_framework import serializers

from .models import Invoice

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', "streetAddress", "city","postCode","country",
                  "clientName", "clientEmail","clientStreetAddress",
                  "clientCity", "clientPostCode", "clientCountry", 
                  "invoiceDate", "paymentTerms", "projectDescription", "invoiceStatus", "markAsPaid",
                  "itemName", "itemQuantity", "itemPrice", "totalPrice"]
        

        

# class SnippetSerializer(serializers.Serializer):
#     #bill form
#     id = serializers.IntegerField(read_only=True)
#     streetAddress = serializers.CharField(max_length=100)
#     city = serializers.CharField(max_length=100)
#     postCode = serializers.CharField(max_length=100)
#     country = serializers.CharField(max_length=100)
#     #Bill to
#     clientName = serializers.CharField(max_length=100)
#     clientEmail = serializers.EmailField(max_length=100)
#     clientStreetAddress = serializers.CharField(max_length=100)
#     clientPostCode = serializers.CharField(max_length=100)
#     clientCountry = serializers.CharField(max_length=100)
#     invoiceDate = serializers.DateField()
#     paymentTerms = serializers.CharField(max_length=100)
#     projectDescription = serializers.CharField(max_length=100)
#     invoiceStatus = serializers.CharField(max_length=100)
#     markAsPaid = serializers.BooleanField(default=False)
#     #items
    

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Invoice.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance