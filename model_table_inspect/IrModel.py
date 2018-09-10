# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class IrModel(models.Model):
    name = models.CharField(max_length=-1)
    model = models.CharField(unique=True, max_length=-1)
    info = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    transient = models.NullBooleanField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    is_mail_thread = models.NullBooleanField()
    website_form_access = models.NullBooleanField()
    website_form_default_field_id = models.IntegerField(blank=True, null=True)
    website_form_label = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model'
