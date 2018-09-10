# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class ProductTemplate(models.Model):
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    description_purchase = models.TextField(blank=True, null=True)
    description_sale = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=-1)
    rental = models.NullBooleanField()
    categ = models.ForeignKey('ProductCategory', models.DO_NOTHING)
    list_price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sale_ok = models.NullBooleanField()
    purchase_ok = models.NullBooleanField()
    uom = models.ForeignKey('ProductUom', models.DO_NOTHING)
    uom_po = models.ForeignKey('ProductUom', models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    active = models.NullBooleanField()
    color = models.IntegerField(blank=True, null=True)
    default_code = models.CharField(max_length=-1, blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    activity_date_deadline = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    l10n_in_hsn_code = models.CharField(max_length=-1, blank=True, null=True)
    service_type = models.CharField(max_length=-1, blank=True, null=True)
    sale_line_warn = models.CharField(max_length=-1)
    sale_line_warn_msg = models.TextField(blank=True, null=True)
    expense_policy = models.CharField(max_length=-1, blank=True, null=True)
    invoice_policy = models.CharField(max_length=-1, blank=True, null=True)
    responsible = models.ForeignKey('ResUsers', models.DO_NOTHING)
    sale_delay = models.FloatField(blank=True, null=True)
    tracking = models.CharField(max_length=-1)
    description_picking = models.TextField(blank=True, null=True)
    description_pickingout = models.TextField(blank=True, null=True)
    description_pickingin = models.TextField(blank=True, null=True)
    website_description = models.TextField(blank=True, null=True)
    rating_last_value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_template'
