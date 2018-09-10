from rest_framework import generics
from ACCOUNTING.models import AccountInvoice
from .serializers import AccountInvoiceJsonSerializer

class AccountInvoiceListView(generics.ListCreateAPIView):
	queryset=AccountInvoice.objects.all()
	serializer_class=AccountInvoiceJsonSerializer
