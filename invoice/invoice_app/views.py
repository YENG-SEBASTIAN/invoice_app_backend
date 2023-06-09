from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Invoice, Item
from .serializers import InvoiceSerializer, ItemSerializer

# Create your views here.
@api_view(['GET'])
def invoice_list(request):
    if request.method == 'GET':
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def create_invoice(request):
    if request.method == "POST":
        data =  request.data
        serializer = InvoiceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def update_invoice(request, pk):
    try:
        invoice = Invoice.objects.get(id=pk)
    except Invoice.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "PUT":
        data = request.data
        serializer = InvoiceSerializer(invoice, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def delete_invoice(request, pk):
    try:
        invoice = Invoice.objects.get(id=pk)
    except Invoice.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "DELETE":
        invoice.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def email_request(request):
    if request.method == "POST":
        data =  request.data
        invoice_serializer = InvoiceSerializer(data=data)
        item_serializer = ItemSerializer(data=data)
        if invoice_serializer.is_valid() and item_serializer.is_valid():
            invoice_serializer.save()
            item_serializer.save()
            
            email = invoice_serializer.data
            user_invoice = Invoice.objects.filter(clientEmail=email['clientEmail'])
            
            context = {
                "user_invoice" : user_invoice,
            }
            return render(request, 'invoice.html', context)
        return Response(invoice_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return render(request, 'invoice.html', context)