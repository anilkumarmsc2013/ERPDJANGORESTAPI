# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class StockPickingType(models.Model):
    name = models.CharField(max_length=-1)
    color = models.IntegerField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    sequence_0 = models.ForeignKey('IrSequence', models.DO_NOTHING, db_column='sequence_id')  # Field renamed because of name conflict.
    default_location_src = models.ForeignKey('StockLocation', models.DO_NOTHING, blank=True, null=True)
    default_location_dest = models.ForeignKey('StockLocation', models.DO_NOTHING, blank=True, null=True)
    code = models.CharField(max_length=-1)
    return_picking_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    show_entire_packs = models.NullBooleanField()
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    active = models.NullBooleanField()
    use_create_lots = models.NullBooleanField()
    use_existing_lots = models.NullBooleanField()
    show_operations = models.NullBooleanField()
    show_reserved = models.NullBooleanField()
    barcode_nomenclature = models.ForeignKey('BarcodeNomenclature', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_picking_type'
