# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class IrModuleModule(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    website = models.CharField(max_length=-1, blank=True, null=True)
    summary = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(unique=True, max_length=-1)
    author = models.CharField(max_length=-1, blank=True, null=True)
    icon = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=16, blank=True, null=True)
    latest_version = models.CharField(max_length=-1, blank=True, null=True)
    shortdesc = models.CharField(max_length=-1, blank=True, null=True)
    category = models.ForeignKey('IrModuleCategory', models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    application = models.NullBooleanField()
    demo = models.NullBooleanField()
    web = models.NullBooleanField()
    license = models.CharField(max_length=32, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    auto_install = models.NullBooleanField()
    maintainer = models.CharField(max_length=-1, blank=True, null=True)
    contributors = models.TextField(blank=True, null=True)
    published_version = models.CharField(max_length=-1, blank=True, null=True)
    url = models.CharField(max_length=-1, blank=True, null=True)
    menus_by_module = models.TextField(blank=True, null=True)
    reports_by_module = models.TextField(blank=True, null=True)
    views_by_module = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_module_module'
