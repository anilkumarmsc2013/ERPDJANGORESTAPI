# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class StockLocation(models.Model):
    parent_left = models.IntegerField(blank=True, null=True)
    parent_right = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    complete_name = models.CharField(max_length=-1, blank=True, null=True)
    active = models.NullBooleanField()
    usage = models.CharField(max_length=-1)
    location = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    posx = models.IntegerField(blank=True, null=True)
    posy = models.IntegerField(blank=True, null=True)
    posz = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    scrap_location = models.NullBooleanField()
    return_location = models.NullBooleanField()
    removal_strategy = models.ForeignKey('ProductRemoval', models.DO_NOTHING, blank=True, null=True)
    putaway_strategy = models.ForeignKey('ProductPutaway', models.DO_NOTHING, blank=True, null=True)
    barcode = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    valuation_in_account = models.ForeignKey('AccountAccount', models.DO_NOTHING, blank=True, null=True)
    valuation_out_account = models.ForeignKey('AccountAccount', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_location'
        unique_together = (('barcode', 'company'),)
