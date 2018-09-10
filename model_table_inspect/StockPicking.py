# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class StockPicking(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    origin = models.CharField(max_length=-1, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    backorder = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    move_type = models.CharField(max_length=-1)
    state = models.CharField(max_length=-1, blank=True, null=True)
    group = models.ForeignKey('ProcurementGroup', models.DO_NOTHING, blank=True, null=True)
    priority = models.CharField(max_length=-1, blank=True, null=True)
    scheduled_date = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    date_done = models.DateTimeField(blank=True, null=True)
    location = models.ForeignKey('StockLocation', models.DO_NOTHING)
    location_dest = models.ForeignKey('StockLocation', models.DO_NOTHING)
    picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    owner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    printed = models.NullBooleanField()
    is_locked = models.NullBooleanField()
    message_last_post = models.DateTimeField(blank=True, null=True)
    activity_date_deadline = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_picking'
        unique_together = (('name', 'company'),)
