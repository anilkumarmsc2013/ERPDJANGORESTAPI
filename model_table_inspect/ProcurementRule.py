# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class ProcurementRule(models.Model):
    name = models.CharField(max_length=-1)
    active = models.NullBooleanField()
    group_propagation_option = models.CharField(max_length=-1, blank=True, null=True)
    group = models.ForeignKey('ProcurementGroup', models.DO_NOTHING, blank=True, null=True)
    action = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey('StockLocation', models.DO_NOTHING, blank=True, null=True)
    location_src = models.ForeignKey('StockLocation', models.DO_NOTHING, blank=True, null=True)
    route = models.ForeignKey('StockLocationRoute', models.DO_NOTHING)
    procure_method = models.CharField(max_length=-1)
    route_sequence = models.IntegerField(blank=True, null=True)
    picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING)
    delay = models.IntegerField(blank=True, null=True)
    partner_address = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    propagate = models.NullBooleanField()
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    propagate_warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procurement_rule'
