# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class StudentPayslip(models.Model):
    fees_structure = models.ForeignKey('StudentFeesStructure', models.DO_NOTHING, blank=True, null=True)
    standard = models.ForeignKey('SchoolStandard', models.DO_NOTHING, blank=True, null=True)
    division = models.ForeignKey('StandardDivision', models.DO_NOTHING, blank=True, null=True)
    medium = models.ForeignKey('StandardMedium', models.DO_NOTHING, blank=True, null=True)
    register = models.ForeignKey('StudentFeesRegister', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    number = models.CharField(max_length=-1, blank=True, null=True)
    student = models.ForeignKey('StudentStudent', models.DO_NOTHING, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True)
    paid_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    due_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    move = models.ForeignKey('AccountMove', models.DO_NOTHING, blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    type = models.CharField(max_length=-1)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_payslip'
        unique_together = (('student', 'date', 'state'),)
