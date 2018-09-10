# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class StockInventory(models.Model):
    name = models.CharField(max_length=-1)
    date = models.DateTimeField()
    state = models.CharField(max_length=-1, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    location = models.ForeignKey('StockLocation', models.DO_NOTHING)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True)
    package = models.ForeignKey('StockQuantPackage', models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    lot = models.ForeignKey('StockProductionLot', models.DO_NOTHING, blank=True, null=True)
    filter = models.CharField(max_length=-1)
    category = models.ForeignKey('ProductCategory', models.DO_NOTHING, blank=True, null=True)
    exhausted = models.NullBooleanField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    accounting_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_inventory'
