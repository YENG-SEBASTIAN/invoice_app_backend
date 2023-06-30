from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.template.loader import render_to_string, get_template
from django.utils.html import strip_tags
from django.conf import settings
from .utils import Utils
from rest_framework import status, generics
from .models import Invoice
from .serializers import InvoiceSerializer

# get all invoices
@api_view(['GET'])
def invoice_list(request):
    if request.method == 'GET':
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_invoice(request, pk):
    try: 
        invoice = Invoice.objects.get(id=pk)
    except Invoice.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = InvoiceSerializer(invoice)
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
            invoice_instace.invoiceStatus = 'Pending'
            # invoice_instace.markAsPaid = True
            invoice_instace.save()
            
            return Response(invoice_serializer.data, status=status.HTTP_201_CREATED)
            # return render(request, 'invoice.html', context)
        return Response(invoice_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return render(request, 'invoice.html')


#create an invoice and save as draft
@api_view(['POST'])
def save_as_draft(request):
    if request.method == "POST":
        data =  request.data
        invoice_serializer = InvoiceSerializer(data=data)
        if invoice_serializer.is_valid():
            invoice_instace = invoice_serializer.save()
            invoice_instace.invoiceStatus = 'Draft'
            invoice_instace.save()
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

    
@api_view(['PUT'])
def mark_as_paid(request, pk):
        try:
            invoice = Invoice.objects.get(id=pk)
        except Invoice.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if request.method == "PUT":
            data = request.data
            serializer = InvoiceSerializer(invoice, data=data, partial = True)
            if serializer.is_valid():
                invoice_instace = serializer.save()
                invoice_instace.markAsPaid = True
                invoice_instace.save()
                serializer.save()
                
                to_email = serializer.data['clientEmail']
                html_content = render_to_string('invoice.html')
                text_content = strip_tags(html_content)
                details = {"to_email":to_email, "text_content":text_content, "html_content":html_content}
                # Utils.send_message(details)
                
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    

#filter by status(Paid)
@api_view(['GET'])
def filter_invoice_paid(request):
    if request.method == 'GET':
        invoices = Invoice.objects.filter(invoiceStatus = 'Paid')
        serializer = InvoiceSerializer(invoices, many=True)
        invoices = serializer.data
        return Response(serializer.data)
    return   Response(status=status.HTTP_404_NOT_FOUND)

#filter by status(Pending)
@api_view(['GET'])
def filter_invoice_pending(request):
    if request.method == 'GET':
        invoices = Invoice.objects.filter(invoiceStatus = 'Pending')
        serializer = InvoiceSerializer(invoices, many=True)
        invoices = serializer.data
        return Response(serializer.data)
    return   Response(status=status.HTTP_404_NOT_FOUND)


#filter by status(Draft)
@api_view(['GET'])
def filter_invoice_draft(request):
    if request.method == 'GET':
        invoices = Invoice.objects.filter(invoiceStatus = 'Draft')
        serializer = InvoiceSerializer(invoices, many=True)
        invoices = serializer.data
        return Response(serializer.data)
    return   Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def filter(request):
    if request.method == "POST":
        data = request.data
        serializer = Filter(data=data) 
        if serializer.is_valid():
            
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)



def email_invoice(request):
    invoice = Invoice.objects.get(id=4)
    total = 0
    for item in invoice.items:
        return render(request, 'invoice.html', context = {
            "items" : invoice.items,
            # "total" : total
            })
    return render(request, 'invoice.html', context = {
            "items" : invoice.items,
            })
    
    # to_email = invoice_serializer.data['clientEmail']
    # html_content = render_to_string('invoice.html')
    # text_content = strip_tags(html_content)
    # details = {"to_email":to_email, "text_content":text_content, "html_content":html_content}
    # Utils.send_message(details)