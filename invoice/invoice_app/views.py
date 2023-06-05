from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Invoice
from .serializers import InvoiceSerializer

# Create your views here.
@api_view(['GET'])
def invoice_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)
