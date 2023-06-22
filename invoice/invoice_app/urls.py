from django.urls import path
from . import views
from .views import (invoice_list, create_invoice, save_and_send, 
                    save_as_draft, save_changes, delete_invoice, filter_invoice_paid, 
                    mark_as_paid, filter_invoice_pending, filter_invoice_draft, email_invoice)

urlpatterns = [
    path('invoice-list/', invoice_list, name='invoices'),
    path('create-invoice/', create_invoice, name='create'),
    path('send-save/', save_and_send, name='send'),
    path('send-draft/', save_as_draft, name='draft'),
    path('mark-paid/<int:pk>/', mark_as_paid, name='paid'),
    path('update-invoice/<int:pk>/', save_changes, name='update'),
    path('delete-invoice/<int:pk>/', delete_invoice, name='delete'),
    path('filter-paid/', filter_invoice_paid, name='filter'),
    path('filter-pending/', filter_invoice_pending, name='filter'),
    path('filter-draft/', filter_invoice_draft, name='filter'),
    path('email/', email_invoice, name='email'),
]