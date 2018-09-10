# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class ResCurrency(models.Model):
    name = models.CharField(unique=True, max_length=-1)
    symbol = models.CharField(max_length=-1)
    rounding = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    active = models.NullBooleanField()
    position = models.CharField(max_length=-1, blank=True, null=True)
    currency_unit_label = models.CharField(max_length=-1, blank=True, null=True)
    currency_subunit_label = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_currency'
