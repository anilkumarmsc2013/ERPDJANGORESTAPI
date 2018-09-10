# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class ResCompany(models.Model):
    name = models.CharField(unique=True, max_length=-1)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    sequence = models.IntegerField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    report_header = models.TextField(blank=True, null=True)
    report_footer = models.TextField(blank=True, null=True)
    logo_web = models.BinaryField(blank=True, null=True)
    account_no = models.CharField(max_length=-1, blank=True, null=True)
    email = models.CharField(max_length=-1, blank=True, null=True)
    phone = models.CharField(max_length=-1, blank=True, null=True)
    company_registry = models.CharField(max_length=-1, blank=True, null=True)
    paperformat = models.ForeignKey('ReportPaperformat', models.DO_NOTHING, blank=True, null=True)
    external_report_layout = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    resource_calendar = models.ForeignKey('ResourceCalendar', models.DO_NOTHING, blank=True, null=True)
    fiscalyear_last_day = models.IntegerField()
    fiscalyear_last_month = models.IntegerField()
    period_lock_date = models.DateField(blank=True, null=True)
    fiscalyear_lock_date = models.DateField(blank=True, null=True)
    transfer_account = models.ForeignKey('AccountAccount', models.DO_NOTHING, blank=True, null=True)
    expects_chart_of_accounts = models.NullBooleanField()
    chart_template = models.ForeignKey('AccountChartTemplate', models.DO_NOTHING, blank=True, null=True)
    bank_account_code_prefix = models.CharField(max_length=-1, blank=True, null=True)
    cash_account_code_prefix = models.CharField(max_length=-1, blank=True, null=True)
    accounts_code_digits = models.IntegerField(blank=True, null=True)
    tax_cash_basis_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True)
    tax_calculation_rounding_method = models.CharField(max_length=-1, blank=True, null=True)
    currency_exchange_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True)
    anglo_saxon_accounting = models.NullBooleanField()
    property_stock_account_input_categ = models.ForeignKey('AccountAccount', models.DO_NOTHING, blank=True, null=True)
    property_stock_account_output_categ = models.ForeignKey('AccountAccount', models.DO_NOTHING, blank=True, null=True)
    property_stock_valuation_account = models.ForeignKey('AccountAccount', models.DO_NOTHING, blank=True, null=True)
    overdue_msg = models.TextField(blank=True, null=True)
    tax_exigibility = models.NullBooleanField()
    account_opening_move = models.ForeignKey('AccountMove', models.DO_NOTHING, blank=True, null=True)
    account_setup_company_data_done = models.NullBooleanField()
    account_setup_bank_data_done = models.NullBooleanField()
    account_setup_fy_data_done = models.NullBooleanField()
    account_setup_coa_done = models.NullBooleanField()
    account_setup_bar_closed = models.NullBooleanField()
    propagation_minimum_delta = models.IntegerField(blank=True, null=True)
    internal_transit_location = models.ForeignKey('StockLocation', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_company'
