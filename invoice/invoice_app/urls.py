from django.urls import path
from . import views

urlpatterns = [
    path('invoice-list/', views.invoice_list, name='invoices'),
    path('create-invoice/', views.create_invoice, name='create'),
    path('update-invoice/<int:pk>/', views.update_invoice, name='update'),
    path('delete-invoice/<int:pk>/', views.delete_invoice, name='delete'),
]