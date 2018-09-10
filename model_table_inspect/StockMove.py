# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class StockMove(models.Model):
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    priority = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField()
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    date_expected = models.DateTimeField()
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING)
    ordered_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product_uom_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    product_uom = models.ForeignKey('ProductUom', models.DO_NOTHING, db_column='product_uom')
    product_packaging = models.ForeignKey('ProductPackaging', models.DO_NOTHING, db_column='product_packaging', blank=True, null=True)
    location = models.ForeignKey('StockLocation', models.DO_NOTHING)
    location_dest = models.ForeignKey('StockLocation', models.DO_NOTHING)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    picking = models.ForeignKey('StockPicking', models.DO_NOTHING, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    price_unit = models.FloatField(blank=True, null=True)
    origin = models.CharField(max_length=-1, blank=True, null=True)
    procure_method = models.CharField(max_length=-1)
    scrapped = models.NullBooleanField()
    group = models.ForeignKey('ProcurementGroup', models.DO_NOTHING, blank=True, null=True)
    rule = models.ForeignKey('ProcurementRule', models.DO_NOTHING, blank=True, null=True)
    push_rule = models.ForeignKey('StockLocationPath', models.DO_NOTHING, blank=True, null=True)
    propagate = models.NullBooleanField()
    picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING, blank=True, null=True)
    inventory = models.ForeignKey('StockInventory', models.DO_NOTHING, blank=True, null=True)
    origin_returned_move = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    restrict_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    additional = models.NullBooleanField()
    reference = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    to_refund = models.NullBooleanField()
    value = models.FloatField(blank=True, null=True)
    remaining_qty = models.FloatField(blank=True, null=True)
    remaining_value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_move'
