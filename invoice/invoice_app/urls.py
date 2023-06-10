from django.urls import path
from . import views

urlpatterns = [
    path('invoice-list/', views.invoice_list, name='invoices'),
    path('create-invoice/', views.create_invoice, name='create'),
    path('send-save/', views.save_and_send, name='send'),
    path('send-draft/', views.save_as_draft, name='draft'),
    path('update-invoice/<int:pk>/', views.save_changes, name='update'),
    path('delete-invoice/<int:pk>/', views.delete_invoice, name='delete'),
]