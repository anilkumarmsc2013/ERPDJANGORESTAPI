# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class LateFeesRule(models.Model):
    fine_type = models.ForeignKey('FineTypes', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    fine_type_0 = models.CharField(db_column='fine_type', max_length=-1, blank=True, null=True)  # Field renamed because of name conflict.
    fine_rate = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    frequency = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'late_fees_rule'
