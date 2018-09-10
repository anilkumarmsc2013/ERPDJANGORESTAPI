# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class StockWarehouse(models.Model):
    name = models.CharField(max_length=-1)
    active = models.NullBooleanField()
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    view_location = models.ForeignKey('StockLocation', models.DO_NOTHING)
    lot_stock = models.ForeignKey('StockLocation', models.DO_NOTHING)
    code = models.CharField(max_length=5)
    reception_steps = models.CharField(max_length=-1)
    delivery_steps = models.CharField(max_length=-1)
    wh_input_stock_loc = models.ForeignKey('StockLocation', models.DO_NOTHING, blank=True, null=True)
    wh_qc_stock_loc = models.ForeignKey('StockLocation', models.DO_NOTHING, blank=True, null=True)
    wh_output_stock_loc = models.ForeignKey('StockLocation', models.DO_NOTHING, blank=True, null=True)
    wh_pack_stock_loc = models.ForeignKey('StockLocation', models.DO_NOTHING, blank=True, null=True)
    mto_pull = models.ForeignKey('ProcurementRule', models.DO_NOTHING, blank=True, null=True)
    pick_type = models.ForeignKey('StockPickingType', models.DO_NOTHING, blank=True, null=True)
    pack_type = models.ForeignKey('StockPickingType', models.DO_NOTHING, blank=True, null=True)
    out_type = models.ForeignKey('StockPickingType', models.DO_NOTHING, blank=True, null=True)
    in_type = models.ForeignKey('StockPickingType', models.DO_NOTHING, blank=True, null=True)
    int_type = models.ForeignKey('StockPickingType', models.DO_NOTHING, blank=True, null=True)
    crossdock_route = models.ForeignKey('StockLocationRoute', models.DO_NOTHING, blank=True, null=True)
    reception_route = models.ForeignKey('StockLocationRoute', models.DO_NOTHING, blank=True, null=True)
    delivery_route = models.ForeignKey('StockLocationRoute', models.DO_NOTHING, blank=True, null=True)
    default_resupply_wh = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_warehouse'
        unique_together = (('code', 'company'), ('name', 'company'),)
