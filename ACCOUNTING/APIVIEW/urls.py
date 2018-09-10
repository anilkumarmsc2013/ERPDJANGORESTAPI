from django.conf.urls import url
from .views import AccountInvoiceListView

urlpatterns = [
    url(r'ListView',AccountInvoiceListView.as_view(),name='ListView'),
]
