from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.template.loader import render_to_string, get_template
from django.utils.html import strip_tags
from django.conf import settings
from .utils import Utils
from rest_framework import status
from .models import Invoice
from .serializers import InvoiceSerializer

# get all invoices
@api_view(['GET'])
def invoice_list(request):
    if request.method == 'GET':
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)

# create an invoice
@api_view(['POST'])
def create_invoice(request):
    if request.method == "POST":
        data =  request.data
        serializer = InvoiceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#create an invoice and send an email
@api_view(['POST'])
def save_and_send(request):
    if request.method == "POST":
        data =  request.data
        invoice_serializer = InvoiceSerializer(data=data)
        if invoice_serializer.is_valid():
            invoice_instace = invoice_serializer.save()
            invoice_instace.invoiceStatus = 'paid'
            invoice_instace.markAsPaid = True
            invoice_instace.save()

            email = invoice_serializer.data
            user_invoice = Invoice.objects.filter(clientEmail=email['clientEmail'])
                  
            context = {
                "user_invoice" : user_invoice,
            }
            
            to_email = invoice_serializer.data['clientEmail']
            html_content = render_to_string('invoice.html', context)
            text_content = strip_tags(html_content)
            details = {"to_email":to_email, "text_content":text_content, "html_content":html_content}
            Utils.send_message(details)
            
            return Response(invoice_serializer.data, status=status.HTTP_201_CREATED)
            # return render(request, 'invoice.html', context)
        return Response(invoice_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return render(request, 'invoice.html', context)

#create an invoice and save as draft
@api_view(['POST'])
def save_as_draft(request):
    if request.method == "POST":
        data =  request.data
        invoice_serializer = InvoiceSerializer(data=data)
        if invoice_serializer.is_valid():
            invoice_serializer.data['invoiceStatus'] = 'draft'
            invoice_serializer.save()            
            return Response(invoice_serializer.data, status=status.HTTP_201_CREATED)
        return Response(invoice_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# update invoice and save changes
@api_view(['PUT'])
def save_changes(request, pk):
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
    

# delete invoice
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
