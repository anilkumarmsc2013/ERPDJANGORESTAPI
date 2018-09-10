from rest_framework import serializers
from ACCOUNTING.models import AccountInvoice

class AccountInvoiceJsonSerializer(serializers.ModelSerializer):
	class Meta:
		model=AccountInvoice
		fields='__all__'
