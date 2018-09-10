# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AccountingAccountinvoicejson(models.Model):
    invoice_id = models.IntegerField()
    invoice_number = models.CharField(max_length=500)
    date_due = models.DateField()
    invoice_date = models.DateField()
    amount = models.FloatField()
    fine = models.FloatField()
    discount = models.FloatField()
    invoice_amount = models.FloatField()

    class Meta:
        managed = False
        db_table = 'ACCOUNTING_accountinvoicejson'


class AcademicMonth(models.Model):
    name = models.CharField(max_length=-1)
    code = models.CharField(max_length=-1)
    date_start = models.DateField()
    date_stop = models.DateField()
    year = models.ForeignKey('AcademicYear', models.DO_NOTHING)
    description = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'academic_month'
        unique_together = (('date_start', 'date_stop', 'year'),)


class AcademicSubject(models.Model):
    add_sub = models.ForeignKey('StudentPreviousSchool', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1)
    maximum_marks = models.IntegerField(blank=True, null=True)
    minimum_marks = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'academic_subject'


class AcademicYear(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    code = models.CharField(max_length=-1)
    date_start = models.DateField()
    date_stop = models.DateField()
    grade = models.ForeignKey('GradeMaster', models.DO_NOTHING, blank=True, null=True)
    current = models.NullBooleanField()
    description = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'academic_year'


class AccountAccount(models.Model):
    name = models.CharField(max_length=-1)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    code = models.CharField(max_length=64)
    deprecated = models.NullBooleanField()
    user_type = models.ForeignKey('AccountAccountType', models.DO_NOTHING)
    internal_type = models.CharField(max_length=-1, blank=True, null=True)
    last_time_entries_checked = models.DateTimeField(blank=True, null=True)
    reconcile = models.NullBooleanField()
    note = models.TextField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    group = models.ForeignKey('AccountGroup', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_account'
        unique_together = (('code', 'company'),)


class AccountAccountAccountTag(models.Model):
    account_account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    account_account_tag = models.ForeignKey('AccountAccountTag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_account_tag'
        unique_together = (('account_account', 'account_account_tag'),)


class AccountAccountFinancialReport(models.Model):
    report_line = models.ForeignKey('AccountFinancialReport', models.DO_NOTHING)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_financial_report'
        unique_together = (('report_line', 'account'),)


class AccountAccountFinancialReportType(models.Model):
    report = models.ForeignKey('AccountFinancialReport', models.DO_NOTHING)
    account_type = models.ForeignKey('AccountAccountType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_financial_report_type'
        unique_together = (('report', 'account_type'),)


class AccountAccountTag(models.Model):
    name = models.CharField(max_length=-1)
    applicability = models.CharField(max_length=-1)
    color = models.IntegerField(blank=True, null=True)
    active = models.NullBooleanField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_account_tag'


class AccountAccountTagAccountTaxTemplateRel(models.Model):
    account_tax_template = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING)
    account_account_tag = models.ForeignKey(AccountAccountTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_tag_account_tax_template_rel'
        unique_together = (('account_tax_template', 'account_account_tag'),)


class AccountAccountTaxDefaultRel(models.Model):
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    tax = models.ForeignKey('AccountTax', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_tax_default_rel'
        unique_together = (('account', 'tax'),)


class AccountAccountTemplate(models.Model):
    name = models.CharField(max_length=-1)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    code = models.CharField(max_length=64)
    user_type = models.ForeignKey('AccountAccountType', models.DO_NOTHING)
    reconcile = models.NullBooleanField()
    note = models.TextField(blank=True, null=True)
    nocreate = models.NullBooleanField()
    chart_template = models.ForeignKey('AccountChartTemplate', models.DO_NOTHING, blank=True, null=True)
    group = models.ForeignKey('AccountGroup', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_account_template'


class AccountAccountTemplateAccountTag(models.Model):
    account_account_template = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING)
    account_account_tag = models.ForeignKey(AccountAccountTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_template_account_tag'
        unique_together = (('account_account_template', 'account_account_tag'),)


class AccountAccountTemplateTaxRel(models.Model):
    account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING)
    tax = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_template_tax_rel'
        unique_together = (('account', 'tax'),)


class AccountAccountType(models.Model):
    name = models.CharField(max_length=-1)
    include_initial_balance = models.NullBooleanField()
    type = models.CharField(max_length=-1)
    note = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_account_type'


class AccountAccountTypeRel(models.Model):
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_type_rel'
        unique_together = (('journal', 'account'),)


class AccountAgedTrialBalance(models.Model):
    result_selection = models.CharField(max_length=-1)
    period_length = models.IntegerField()
    date_from = models.DateField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    target_move = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_aged_trial_balance'


class AccountAgedTrialBalanceAccountJournalRel(models.Model):
    account_aged_trial_balance = models.ForeignKey(AccountAgedTrialBalance, models.DO_NOTHING)
    account_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_aged_trial_balance_account_journal_rel'
        unique_together = (('account_aged_trial_balance', 'account_journal'),)


class AccountAnalyticAccount(models.Model):
    name = models.CharField(max_length=-1)
    code = models.CharField(max_length=-1, blank=True, null=True)
    active = models.NullBooleanField()
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_account'


class AccountAnalyticAccountTagRel(models.Model):
    account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING)
    tag = models.ForeignKey('AccountAnalyticTag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_analytic_account_tag_rel'
        unique_together = (('account', 'tag'),)


class AccountAnalyticLine(models.Model):
    name = models.CharField(max_length=-1)
    date = models.DateField()
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    unit_amount = models.FloatField(blank=True, null=True)
    account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    product_uom = models.ForeignKey('ProductUom', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True)
    general_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    move = models.ForeignKey('AccountMoveLine', models.DO_NOTHING, blank=True, null=True)
    code = models.CharField(max_length=8, blank=True, null=True)
    ref = models.CharField(max_length=-1, blank=True, null=True)
    amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_line'


class AccountAnalyticLineTagRel(models.Model):
    line = models.ForeignKey(AccountAnalyticLine, models.DO_NOTHING)
    tag = models.ForeignKey('AccountAnalyticTag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_analytic_line_tag_rel'
        unique_together = (('line', 'tag'),)


class AccountAnalyticTag(models.Model):
    name = models.CharField(max_length=-1)
    color = models.IntegerField(blank=True, null=True)
    active = models.NullBooleanField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_tag'


class AccountAnalyticTagAccountInvoiceLineRel(models.Model):
    account_invoice_line = models.ForeignKey('AccountInvoiceLine', models.DO_NOTHING)
    account_analytic_tag = models.ForeignKey(AccountAnalyticTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_analytic_tag_account_invoice_line_rel'
        unique_together = (('account_invoice_line', 'account_analytic_tag'),)


class AccountAnalyticTagAccountMoveLineRel(models.Model):
    account_move_line = models.ForeignKey('AccountMoveLine', models.DO_NOTHING)
    account_analytic_tag = models.ForeignKey(AccountAnalyticTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_analytic_tag_account_move_line_rel'
        unique_together = (('account_move_line', 'account_analytic_tag'),)


class AccountBalanceReport(models.Model):
    display_account = models.CharField(max_length=-1)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    target_move = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_balance_report'


class AccountBalanceReportJournalRel(models.Model):
    account = models.ForeignKey(AccountBalanceReport, models.DO_NOTHING)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_balance_report_journal_rel'
        unique_together = (('account', 'journal'),)


class AccountBankAccountsWizard(models.Model):
    acc_name = models.CharField(max_length=-1)
    bank_account = models.ForeignKey('WizardMultiChartsAccounts', models.DO_NOTHING)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    account_type = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_bank_accounts_wizard'


class AccountBankStatement(models.Model):
    message_last_post = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    reference = models.CharField(max_length=-1, blank=True, null=True)
    date = models.DateField()
    date_done = models.DateTimeField(blank=True, null=True)
    balance_start = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    balance_end_real = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    state = models.CharField(max_length=-1)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    total_entry_encoding = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    balance_end = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    difference = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    cashbox_start = models.ForeignKey('AccountBankStatementCashbox', models.DO_NOTHING, blank=True, null=True)
    cashbox_end = models.ForeignKey('AccountBankStatementCashbox', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_bank_statement'


class AccountBankStatementCashbox(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_bank_statement_cashbox'


class AccountBankStatementClosebalance(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_bank_statement_closebalance'


class AccountBankStatementImport(models.Model):
    data_file = models.BinaryField()
    filename = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_bank_statement_import'


class AccountBankStatementImportJournalCreation(models.Model):
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_bank_statement_import_journal_creation'


class AccountBankStatementLine(models.Model):
    name = models.CharField(max_length=-1)
    date = models.DateField()
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    bank_account = models.ForeignKey('ResPartnerBank', models.DO_NOTHING, blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    statement = models.ForeignKey(AccountBankStatement, models.DO_NOTHING)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True)
    partner_name = models.CharField(max_length=-1, blank=True, null=True)
    ref = models.CharField(max_length=-1, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    move_name = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    unique_import_id = models.CharField(unique=True, max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_bank_statement_line'


class AccountCashRounding(models.Model):
    name = models.CharField(max_length=-1)
    rounding = models.FloatField()
    strategy = models.CharField(max_length=-1)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    rounding_method = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_cash_rounding'


class AccountCashboxLine(models.Model):
    coin_value = models.DecimalField(max_digits=65535, decimal_places=65535)
    number = models.IntegerField(blank=True, null=True)
    cashbox = models.ForeignKey(AccountBankStatementCashbox, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_cashbox_line'


class AccountChartTemplate(models.Model):
    name = models.CharField(max_length=-1)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    code_digits = models.IntegerField()
    visible = models.NullBooleanField()
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    use_anglo_saxon = models.NullBooleanField()
    complete_tax_set = models.NullBooleanField()
    bank_account_code_prefix = models.CharField(max_length=-1, blank=True, null=True)
    cash_account_code_prefix = models.CharField(max_length=-1, blank=True, null=True)
    transfer_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING)
    income_currency_exchange_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    expense_currency_exchange_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_account_receivable = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_account_payable = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_account_expense_categ = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_account_income_categ = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_account_expense = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_account_income = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_stock_account_input_categ = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_stock_account_output_categ = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_stock_valuation_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_chart_template'


class AccountCommonAccountReport(models.Model):
    display_account = models.CharField(max_length=-1)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    target_move = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_common_account_report'


class AccountCommonAccountReportAccountJournalRel(models.Model):
    account_common_account_report = models.ForeignKey(AccountCommonAccountReport, models.DO_NOTHING)
    account_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_common_account_report_account_journal_rel'
        unique_together = (('account_common_account_report', 'account_journal'),)


class AccountCommonJournalReport(models.Model):
    amount_currency = models.NullBooleanField()
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    target_move = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_common_journal_report'


class AccountCommonJournalReportAccountJournalRel(models.Model):
    account_common_journal_report = models.ForeignKey(AccountCommonJournalReport, models.DO_NOTHING)
    account_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_common_journal_report_account_journal_rel'
        unique_together = (('account_common_journal_report', 'account_journal'),)


class AccountCommonPartnerReport(models.Model):
    result_selection = models.CharField(max_length=-1)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    target_move = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_common_partner_report'


class AccountCommonPartnerReportAccountJournalRel(models.Model):
    account_common_partner_report = models.ForeignKey(AccountCommonPartnerReport, models.DO_NOTHING)
    account_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_common_partner_report_account_journal_rel'
        unique_together = (('account_common_partner_report', 'account_journal'),)


class AccountCommonReport(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    target_move = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_common_report'


class AccountCommonReportAccountJournalRel(models.Model):
    account_common_report = models.ForeignKey(AccountCommonReport, models.DO_NOTHING)
    account_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_common_report_account_journal_rel'
        unique_together = (('account_common_report', 'account_journal'),)


class AccountFinancialReport(models.Model):
    name = models.CharField(max_length=-1)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=-1, blank=True, null=True)
    account_report = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    sign = models.IntegerField()
    display_detail = models.CharField(max_length=-1, blank=True, null=True)
    style_overwrite = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_financial_report'


class AccountFinancialYearOp(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_financial_year_op'


class AccountFiscalPosition(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    active = models.NullBooleanField()
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    auto_apply = models.NullBooleanField()
    vat_required = models.NullBooleanField()
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True)
    country_group = models.ForeignKey('ResCountryGroup', models.DO_NOTHING, blank=True, null=True)
    zip_from = models.IntegerField(blank=True, null=True)
    zip_to = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position'


class AccountFiscalPositionAccount(models.Model):
    position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING)
    account_src = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    account_dest = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_account'
        unique_together = (('position', 'account_src', 'account_dest'),)


class AccountFiscalPositionAccountTemplate(models.Model):
    position = models.ForeignKey('AccountFiscalPositionTemplate', models.DO_NOTHING)
    account_src = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING)
    account_dest = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_account_template'


class AccountFiscalPositionResCountryStateRel(models.Model):
    account_fiscal_position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING)
    res_country_state = models.ForeignKey('ResCountryState', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_res_country_state_rel'
        unique_together = (('account_fiscal_position', 'res_country_state'),)


class AccountFiscalPositionTax(models.Model):
    position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING)
    tax_src = models.ForeignKey('AccountTax', models.DO_NOTHING)
    tax_dest = models.ForeignKey('AccountTax', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_tax'
        unique_together = (('position', 'tax_src', 'tax_dest'),)


class AccountFiscalPositionTaxTemplate(models.Model):
    position = models.ForeignKey('AccountFiscalPositionTemplate', models.DO_NOTHING)
    tax_src = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING)
    tax_dest = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_tax_template'


class AccountFiscalPositionTemplate(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    chart_template = models.ForeignKey(AccountChartTemplate, models.DO_NOTHING)
    note = models.TextField(blank=True, null=True)
    auto_apply = models.NullBooleanField()
    vat_required = models.NullBooleanField()
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True)
    country_group = models.ForeignKey('ResCountryGroup', models.DO_NOTHING, blank=True, null=True)
    zip_from = models.IntegerField(blank=True, null=True)
    zip_to = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_template'


class AccountFiscalPositionTemplateResCountryStateRel(models.Model):
    account_fiscal_position_template = models.ForeignKey(AccountFiscalPositionTemplate, models.DO_NOTHING)
    res_country_state = models.ForeignKey('ResCountryState', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_template_res_country_state_rel'
        unique_together = (('account_fiscal_position_template', 'res_country_state'),)


class AccountFullReconcile(models.Model):
    name = models.CharField(max_length=-1)
    exchange_move = models.ForeignKey('AccountMove', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_full_reconcile'


class AccountGroup(models.Model):
    parent_left = models.IntegerField(blank=True, null=True)
    parent_right = models.IntegerField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1)
    code_prefix = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_group'


class AccountInvoice(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    origin = models.CharField(max_length=-1, blank=True, null=True)
    type = models.CharField(max_length=-1, blank=True, null=True)
    access_token = models.CharField(max_length=-1, blank=True, null=True)
    refund_invoice = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    number = models.CharField(max_length=-1, blank=True, null=True)
    move_name = models.CharField(max_length=-1, blank=True, null=True)
    reference = models.CharField(max_length=-1, blank=True, null=True)
    reference_type = models.CharField(max_length=-1)
    comment = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    sent = models.NullBooleanField()
    date_invoice = models.DateField(blank=True, null=True)
    date_due = models.DateField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    payment_term = models.ForeignKey('AccountPaymentTerm', models.DO_NOTHING, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    move = models.ForeignKey('AccountMove', models.DO_NOTHING, blank=True, null=True)
    amount_untaxed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_untaxed_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_tax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_total_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_total_company_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    reconciled = models.NullBooleanField()
    partner_bank = models.ForeignKey('ResPartnerBank', models.DO_NOTHING, blank=True, null=True)
    residual = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    residual_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    residual_company_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    fiscal_position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING, blank=True, null=True)
    commercial_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    cash_rounding = models.ForeignKey(AccountCashRounding, models.DO_NOTHING, blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    activity_date_deadline = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    slip_ref = models.CharField(max_length=-1, blank=True, null=True)
    student_payslip = models.ForeignKey('StudentPayslip', models.DO_NOTHING, blank=True, null=True)
    student_bulk_payslip = models.ForeignKey('StudentFeesRegister', models.DO_NOTHING, blank=True, null=True)
    student_fine = models.FloatField(blank=True, null=True)
    fine_type = models.ForeignKey('LateFeesRule', models.DO_NOTHING, blank=True, null=True)
    fine_type_0 = models.CharField(db_column='fine_type', max_length=-1, blank=True, null=True)  # Field renamed because of name conflict.
    fine_rate = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_fine = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    due_date_reminder = models.NullBooleanField()
    fine_apply_flag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_invoice'
        unique_together = (('number', 'company', 'journal', 'type'),)


class AccountInvoiceAccountMoveLineRel(models.Model):
    account_invoice = models.ForeignKey(AccountInvoice, models.DO_NOTHING)
    account_move_line = models.ForeignKey('AccountMoveLine', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_invoice_account_move_line_rel'
        unique_together = (('account_invoice', 'account_move_line'),)


class AccountInvoiceAccountRegisterPaymentsRel(models.Model):
    account_register_payments = models.ForeignKey('AccountRegisterPayments', models.DO_NOTHING)
    account_invoice = models.ForeignKey(AccountInvoice, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_invoice_account_register_payments_rel'
        unique_together = (('account_register_payments', 'account_invoice'),)


class AccountInvoiceConfirm(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_invoice_confirm'


class AccountInvoiceLine(models.Model):
    name = models.TextField()
    origin = models.CharField(max_length=-1, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    invoice = models.ForeignKey(AccountInvoice, models.DO_NOTHING, blank=True, null=True)
    uom = models.ForeignKey('ProductUom', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535)
    price_subtotal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_subtotal_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535)
    discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    account_analytic = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    is_rounding_line = models.NullBooleanField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    discount2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    discount3 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_invoice_line'


class AccountInvoiceLineTax(models.Model):
    invoice_line = models.ForeignKey(AccountInvoiceLine, models.DO_NOTHING)
    tax = models.ForeignKey('AccountTax', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_invoice_line_tax'
        unique_together = (('invoice_line', 'tax'),)


class AccountInvoicePaymentRel(models.Model):
    payment = models.ForeignKey('AccountPayment', models.DO_NOTHING)
    invoice = models.ForeignKey(AccountInvoice, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_invoice_payment_rel'
        unique_together = (('payment', 'invoice'),)


class AccountInvoiceRefund(models.Model):
    date_invoice = models.DateField()
    date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=-1)
    filter_refund = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_invoice_refund'


class AccountInvoiceTax(models.Model):
    invoice = models.ForeignKey(AccountInvoice, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1)
    tax = models.ForeignKey('AccountTax', models.DO_NOTHING, blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    account_analytic = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_rounding = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    manual = models.NullBooleanField()
    sequence = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    base = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_invoice_tax'


class AccountJournal(models.Model):
    name = models.CharField(max_length=-1)
    code = models.CharField(max_length=5)
    active = models.NullBooleanField()
    type = models.CharField(max_length=-1)
    default_credit_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    default_debit_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    update_posted = models.NullBooleanField()
    group_invoice_lines = models.NullBooleanField()
    sequence = models.ForeignKey('IrSequence', models.DO_NOTHING)
    refund_sequence = models.ForeignKey('IrSequence', models.DO_NOTHING, blank=True, null=True)
    sequence_0 = models.IntegerField(db_column='sequence', blank=True, null=True)  # Field renamed because of name conflict.
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    refund_sequence_0 = models.NullBooleanField(db_column='refund_sequence')  # Field renamed because of name conflict.
    at_least_one_inbound = models.NullBooleanField()
    at_least_one_outbound = models.NullBooleanField()
    profit_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    loss_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    bank_account = models.ForeignKey('ResPartnerBank', models.DO_NOTHING, blank=True, null=True)
    bank_statements_source = models.CharField(max_length=-1, blank=True, null=True)
    show_on_dashboard = models.NullBooleanField()
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_journal'
        unique_together = (('code', 'name', 'company'),)


class AccountJournalAccountPrintJournalRel(models.Model):
    account_print_journal = models.ForeignKey('AccountPrintJournal', models.DO_NOTHING)
    account_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_journal_account_print_journal_rel'
        unique_together = (('account_print_journal', 'account_journal'),)


class AccountJournalAccountReportPartnerLedgerRel(models.Model):
    account_report_partner_ledger = models.ForeignKey('AccountReportPartnerLedger', models.DO_NOTHING)
    account_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_journal_account_report_partner_ledger_rel'
        unique_together = (('account_report_partner_ledger', 'account_journal'),)


class AccountJournalAccountTaxReportRel(models.Model):
    account_tax_report = models.ForeignKey('AccountTaxReport', models.DO_NOTHING)
    account_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_journal_account_tax_report_rel'
        unique_together = (('account_tax_report', 'account_journal'),)


class AccountJournalAccountingReportRel(models.Model):
    accounting_report = models.ForeignKey('AccountingReport', models.DO_NOTHING)
    account_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_journal_accounting_report_rel'
        unique_together = (('accounting_report', 'account_journal'),)


class AccountJournalInboundPaymentMethodRel(models.Model):
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    inbound_payment_method = models.ForeignKey('AccountPaymentMethod', models.DO_NOTHING, db_column='inbound_payment_method')

    class Meta:
        managed = False
        db_table = 'account_journal_inbound_payment_method_rel'
        unique_together = (('journal', 'inbound_payment_method'),)


class AccountJournalOutboundPaymentMethodRel(models.Model):
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    outbound_payment_method = models.ForeignKey('AccountPaymentMethod', models.DO_NOTHING, db_column='outbound_payment_method')

    class Meta:
        managed = False
        db_table = 'account_journal_outbound_payment_method_rel'
        unique_together = (('journal', 'outbound_payment_method'),)


class AccountJournalTypeRel(models.Model):
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    type = models.ForeignKey(AccountAccountType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_journal_type_rel'
        unique_together = (('journal', 'type'),)


class AccountMove(models.Model):
    name = models.CharField(max_length=-1)
    ref = models.CharField(max_length=-1, blank=True, null=True)
    date = models.DateField()
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=-1)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    narration = models.TextField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    matched_percentage = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tax_cash_basis_rec = models.ForeignKey('AccountPartialReconcile', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    stock_move = models.ForeignKey('StockMove', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_move'


class AccountMoveLine(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product_uom = models.ForeignKey('ProductUom', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True)
    debit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    credit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    balance = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    debit_cash_basis = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    credit_cash_basis = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    balance_cash_basis = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    company_currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    amount_residual = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_residual_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tax_base_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    move = models.ForeignKey(AccountMove, models.DO_NOTHING)
    ref = models.CharField(max_length=-1, blank=True, null=True)
    payment = models.ForeignKey('AccountPayment', models.DO_NOTHING, blank=True, null=True)
    statement_line = models.ForeignKey(AccountBankStatementLine, models.DO_NOTHING, blank=True, null=True)
    statement = models.ForeignKey(AccountBankStatement, models.DO_NOTHING, blank=True, null=True)
    reconciled = models.NullBooleanField()
    full_reconcile = models.ForeignKey(AccountFullReconcile, models.DO_NOTHING, blank=True, null=True)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True)
    blocked = models.NullBooleanField()
    date_maturity = models.DateField()
    date = models.DateField(blank=True, null=True)
    tax_line = models.ForeignKey('AccountTax', models.DO_NOTHING, blank=True, null=True)
    analytic_account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    invoice = models.ForeignKey(AccountInvoice, models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    user_type = models.ForeignKey(AccountAccountType, models.DO_NOTHING, blank=True, null=True)
    tax_exigible = models.NullBooleanField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_move_line'


class AccountMoveLineAccountTaxRel(models.Model):
    account_move_line = models.ForeignKey(AccountMoveLine, models.DO_NOTHING)
    account_tax = models.ForeignKey('AccountTax', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_move_line_account_tax_rel'
        unique_together = (('account_move_line', 'account_tax'),)


class AccountMoveLineReconcile(models.Model):
    trans_nbr = models.IntegerField(blank=True, null=True)
    credit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    debit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    writeoff = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_move_line_reconcile'


class AccountMoveLineReconcileWriteoff(models.Model):
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    writeoff_acc = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    date_p = models.DateField(blank=True, null=True)
    comment = models.CharField(max_length=-1)
    analytic = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_move_line_reconcile_writeoff'


class AccountMoveReversal(models.Model):
    date = models.DateField()
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_move_reversal'


class AccountOpening(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_opening'


class AccountPartialReconcile(models.Model):
    debit_move = models.ForeignKey(AccountMoveLine, models.DO_NOTHING)
    credit_move = models.ForeignKey(AccountMoveLine, models.DO_NOTHING)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    full_reconcile = models.ForeignKey(AccountFullReconcile, models.DO_NOTHING, blank=True, null=True)
    max_date = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_partial_reconcile'


class AccountPayment(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    payment_type = models.CharField(max_length=-1)
    payment_reference = models.CharField(max_length=-1, blank=True, null=True)
    move_name = models.CharField(max_length=-1, blank=True, null=True)
    destination_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True)
    payment_difference_handling = models.CharField(max_length=-1, blank=True, null=True)
    writeoff_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    writeoff_label = models.CharField(max_length=-1, blank=True, null=True)
    payment_method = models.ForeignKey('AccountPaymentMethod', models.DO_NOTHING)
    partner_type = models.CharField(max_length=-1, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    payment_date = models.DateField()
    communication = models.CharField(max_length=-1, blank=True, null=True)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    message_last_post = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    payment_transaction = models.ForeignKey('PaymentTransaction', models.DO_NOTHING, blank=True, null=True)
    payment_token = models.ForeignKey('PaymentToken', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_payment'


class AccountPaymentMethod(models.Model):
    name = models.CharField(max_length=-1)
    code = models.CharField(max_length=-1)
    payment_type = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_payment_method'


class AccountPaymentTerm(models.Model):
    name = models.CharField(max_length=-1)
    active = models.NullBooleanField()
    note = models.TextField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    sequence = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_payment_term'


class AccountPaymentTermLine(models.Model):
    value = models.CharField(max_length=-1)
    value_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    days = models.IntegerField()
    option = models.CharField(max_length=-1)
    payment = models.ForeignKey(AccountPaymentTerm, models.DO_NOTHING)
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_payment_term_line'


class AccountPrintJournal(models.Model):
    sort_selection = models.CharField(max_length=-1)
    amount_currency = models.NullBooleanField()
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    target_move = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_print_journal'


class AccountReconcileModel(models.Model):
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField()
    has_second_line = models.NullBooleanField()
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True)
    label = models.CharField(max_length=-1, blank=True, null=True)
    amount_type = models.CharField(max_length=-1)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    tax = models.ForeignKey('AccountTax', models.DO_NOTHING, blank=True, null=True)
    analytic_account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    second_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    second_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True)
    second_label = models.CharField(max_length=-1, blank=True, null=True)
    second_amount_type = models.CharField(max_length=-1)
    second_amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    second_tax = models.ForeignKey('AccountTax', models.DO_NOTHING, blank=True, null=True)
    second_analytic_account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model'


class AccountReconcileModelTemplate(models.Model):
    chart_template = models.ForeignKey(AccountChartTemplate, models.DO_NOTHING)
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField()
    has_second_line = models.NullBooleanField()
    account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    label = models.CharField(max_length=-1, blank=True, null=True)
    amount_type = models.CharField(max_length=-1)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    tax = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING, blank=True, null=True)
    second_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    second_label = models.CharField(max_length=-1, blank=True, null=True)
    second_amount_type = models.CharField(max_length=-1)
    second_amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    second_tax = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_template'


class AccountRegisterPayments(models.Model):
    multi = models.NullBooleanField()
    payment_type = models.CharField(max_length=-1)
    payment_method = models.ForeignKey(AccountPaymentMethod, models.DO_NOTHING)
    partner_type = models.CharField(max_length=-1, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    payment_date = models.DateField()
    communication = models.CharField(max_length=-1, blank=True, null=True)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_register_payments'


class AccountReportGeneralLedger(models.Model):
    display_account = models.CharField(max_length=-1)
    initial_balance = models.NullBooleanField()
    sortby = models.CharField(max_length=-1)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    target_move = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_report_general_ledger'


class AccountReportGeneralLedgerJournalRel(models.Model):
    account = models.ForeignKey(AccountReportGeneralLedger, models.DO_NOTHING)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_report_general_ledger_journal_rel'
        unique_together = (('account', 'journal'),)


class AccountReportPartnerLedger(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    target_move = models.CharField(max_length=-1)
    result_selection = models.CharField(max_length=-1)
    amount_currency = models.NullBooleanField()
    reconciled = models.NullBooleanField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_report_partner_ledger'


class AccountTax(models.Model):
    name = models.CharField(max_length=-1)
    type_tax_use = models.CharField(max_length=-1)
    tax_adjustment = models.NullBooleanField()
    amount_type = models.CharField(max_length=-1)
    active = models.NullBooleanField()
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    sequence = models.IntegerField()
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    refund_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=-1, blank=True, null=True)
    price_include = models.NullBooleanField()
    include_base_amount = models.NullBooleanField()
    analytic = models.NullBooleanField()
    tax_group = models.ForeignKey('AccountTaxGroup', models.DO_NOTHING)
    tax_exigibility = models.CharField(max_length=-1, blank=True, null=True)
    cash_basis_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, db_column='cash_basis_account', blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    cash_basis_base_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    python_compute = models.TextField(blank=True, null=True)
    python_applicable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tax'
        unique_together = (('name', 'company', 'type_tax_use'),)


class AccountTaxAccountTag(models.Model):
    account_tax = models.ForeignKey(AccountTax, models.DO_NOTHING)
    account_account_tag = models.ForeignKey(AccountAccountTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_tax_account_tag'
        unique_together = (('account_tax', 'account_account_tag'),)


class AccountTaxFiliationRel(models.Model):
    parent_tax = models.ForeignKey(AccountTax, models.DO_NOTHING, db_column='parent_tax')
    child_tax = models.ForeignKey(AccountTax, models.DO_NOTHING, db_column='child_tax')

    class Meta:
        managed = False
        db_table = 'account_tax_filiation_rel'
        unique_together = (('parent_tax', 'child_tax'),)


class AccountTaxGroup(models.Model):
    name = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tax_group'


class AccountTaxReport(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    target_move = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tax_report'


class AccountTaxStudentPayslipInvoicelineRel(models.Model):
    student_payslip_invoiceline = models.ForeignKey('StudentPayslipInvoiceline', models.DO_NOTHING)
    account_tax = models.ForeignKey(AccountTax, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_tax_student_payslip_invoiceline_rel'
        unique_together = (('student_payslip_invoiceline', 'account_tax'),)


class AccountTaxStudentPayslipLineRel(models.Model):
    student_payslip_line = models.ForeignKey('StudentPayslipLine', models.DO_NOTHING)
    account_tax = models.ForeignKey(AccountTax, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_tax_student_payslip_line_rel'
        unique_together = (('student_payslip_line', 'account_tax'),)


class AccountTaxTemplate(models.Model):
    chart_template = models.ForeignKey(AccountChartTemplate, models.DO_NOTHING)
    name = models.CharField(max_length=-1)
    type_tax_use = models.CharField(max_length=-1)
    tax_adjustment = models.NullBooleanField()
    amount_type = models.CharField(max_length=-1)
    active = models.NullBooleanField()
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField()
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    refund_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=-1, blank=True, null=True)
    price_include = models.NullBooleanField()
    include_base_amount = models.NullBooleanField()
    analytic = models.NullBooleanField()
    tax_group = models.ForeignKey(AccountTaxGroup, models.DO_NOTHING, blank=True, null=True)
    tax_exigibility = models.CharField(max_length=-1, blank=True, null=True)
    cash_basis_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, db_column='cash_basis_account', blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    python_compute = models.TextField(blank=True, null=True)
    python_applicable = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tax_template'
        unique_together = (('name', 'company', 'type_tax_use', 'chart_template'),)


class AccountTaxTemplateFiliationRel(models.Model):
    parent_tax = models.ForeignKey(AccountTaxTemplate, models.DO_NOTHING, db_column='parent_tax')
    child_tax = models.ForeignKey(AccountTaxTemplate, models.DO_NOTHING, db_column='child_tax')

    class Meta:
        managed = False
        db_table = 'account_tax_template_filiation_rel'
        unique_together = (('parent_tax', 'child_tax'),)


class AccountUnreconcile(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_unreconcile'


class AccountingReport(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    target_move = models.CharField(max_length=-1)
    enable_filter = models.NullBooleanField()
    account_report = models.ForeignKey(AccountFinancialReport, models.DO_NOTHING)
    label_filter = models.CharField(max_length=-1, blank=True, null=True)
    filter_cmp = models.CharField(max_length=-1)
    date_from_cmp = models.DateField(blank=True, null=True)
    date_to_cmp = models.DateField(blank=True, null=True)
    debit_credit = models.NullBooleanField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounting_report'


class AssignRollNo(models.Model):
    standard = models.ForeignKey('SchoolStandard', models.DO_NOTHING)
    medium = models.ForeignKey('StandardMedium', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assign_roll_no'


class AttendanceType(models.Model):
    name = models.CharField(max_length=-1)
    code = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attendance_type'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BarcodeNomenclature(models.Model):
    name = models.CharField(max_length=32)
    upc_ean_conv = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'barcode_nomenclature'


class BarcodeRule(models.Model):
    name = models.CharField(max_length=32)
    barcode_nomenclature = models.ForeignKey(BarcodeNomenclature, models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    encoding = models.CharField(max_length=-1)
    type = models.CharField(max_length=-1)
    pattern = models.CharField(max_length=32)
    alias = models.CharField(max_length=32)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'barcode_rule'


class BaseImportImport(models.Model):
    res_model = models.CharField(max_length=-1, blank=True, null=True)
    file = models.BinaryField(blank=True, null=True)
    file_name = models.CharField(max_length=-1, blank=True, null=True)
    file_type = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_import'


class BaseImportTestsModelsChar(models.Model):
    value = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char'


class BaseImportTestsModelsCharNoreadonly(models.Model):
    value = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_noreadonly'


class BaseImportTestsModelsCharReadonly(models.Model):
    value = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_readonly'


class BaseImportTestsModelsCharRequired(models.Model):
    value = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_required'


class BaseImportTestsModelsCharStates(models.Model):
    value = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_states'


class BaseImportTestsModelsCharStillreadonly(models.Model):
    value = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_stillreadonly'


class BaseImportTestsModelsM2O(models.Model):
    value = models.ForeignKey('BaseImportTestsModelsM2ORelated', models.DO_NOTHING, db_column='value', blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_m2o'


class BaseImportTestsModelsM2ORelated(models.Model):
    value = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_m2o_related'


class BaseImportTestsModelsM2ORequired(models.Model):
    value = models.ForeignKey('BaseImportTestsModelsM2ORequiredRelated', models.DO_NOTHING, db_column='value')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_m2o_required'


class BaseImportTestsModelsM2ORequiredRelated(models.Model):
    value = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_m2o_required_related'


class BaseImportTestsModelsO2M(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_o2m'


class BaseImportTestsModelsO2MChild(models.Model):
    parent = models.ForeignKey(BaseImportTestsModelsO2M, models.DO_NOTHING, blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_o2m_child'


class BaseImportTestsModelsPreview(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    somevalue = models.IntegerField()
    othervalue = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_preview'


class BaseLanguageExport(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    lang = models.CharField(max_length=-1)
    format = models.CharField(max_length=-1)
    data = models.BinaryField(blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_language_export'


class BaseLanguageImport(models.Model):
    name = models.CharField(max_length=-1)
    code = models.CharField(max_length=5)
    data = models.BinaryField()
    filename = models.CharField(max_length=-1)
    overwrite = models.NullBooleanField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_language_import'


class BaseLanguageInstall(models.Model):
    lang = models.CharField(max_length=-1)
    overwrite = models.NullBooleanField()
    state = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_language_install'


class BaseModuleUninstall(models.Model):
    show_all = models.NullBooleanField()
    module = models.ForeignKey('IrModuleModule', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_module_uninstall'


class BaseModuleUpdate(models.Model):
    updated = models.IntegerField(blank=True, null=True)
    added = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_module_update'


class BaseModuleUpgrade(models.Model):
    module_info = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_module_upgrade'


class BaseUpdateTranslations(models.Model):
    lang = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_update_translations'


class BusBus(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    channel = models.CharField(max_length=-1, blank=True, null=True)
    message = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bus_bus'


class BusPresence(models.Model):
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, unique=True)
    last_poll = models.DateTimeField(blank=True, null=True)
    last_presence = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bus_presence'


class CalendarAlarm(models.Model):
    name = models.CharField(max_length=-1)
    type = models.CharField(max_length=-1)
    duration = models.IntegerField()
    interval = models.CharField(max_length=-1)
    duration_minutes = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_alarm'


class CalendarAlarmCalendarEventRel(models.Model):
    calendar_event = models.ForeignKey('CalendarEvent', models.DO_NOTHING)
    calendar_alarm = models.ForeignKey(CalendarAlarm, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'calendar_alarm_calendar_event_rel'
        unique_together = (('calendar_event', 'calendar_alarm'),)


class CalendarAttendee(models.Model):
    state = models.CharField(max_length=-1, blank=True, null=True)
    common_name = models.CharField(max_length=-1, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    email = models.CharField(max_length=-1, blank=True, null=True)
    availability = models.CharField(max_length=-1, blank=True, null=True)
    access_token = models.CharField(max_length=-1, blank=True, null=True)
    event = models.ForeignKey('CalendarEvent', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_attendee'


class CalendarContacts(models.Model):
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    active = models.NullBooleanField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_contacts'
        unique_together = (('user', 'partner'),)


class CalendarEvent(models.Model):
    name = models.CharField(max_length=-1)
    state = models.CharField(max_length=-1, blank=True, null=True)
    display_start = models.CharField(max_length=-1, blank=True, null=True)
    start = models.DateTimeField()
    stop = models.DateTimeField()
    allday = models.NullBooleanField()
    start_date = models.DateField(blank=True, null=True)
    start_datetime = models.DateTimeField(blank=True, null=True)
    stop_date = models.DateField(blank=True, null=True)
    stop_datetime = models.DateTimeField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    privacy = models.CharField(max_length=-1, blank=True, null=True)
    location = models.CharField(max_length=-1, blank=True, null=True)
    show_as = models.CharField(max_length=-1, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    res_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    res_model_0 = models.CharField(db_column='res_model', max_length=-1, blank=True, null=True)  # Field renamed because of name conflict.
    rrule = models.CharField(max_length=-1, blank=True, null=True)
    rrule_type = models.CharField(max_length=-1, blank=True, null=True)
    recurrency = models.NullBooleanField()
    recurrent_id = models.IntegerField(blank=True, null=True)
    recurrent_id_date = models.DateTimeField(blank=True, null=True)
    end_type = models.CharField(max_length=-1, blank=True, null=True)
    interval = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    mo = models.NullBooleanField()
    tu = models.NullBooleanField()
    we = models.NullBooleanField()
    th = models.NullBooleanField()
    fr = models.NullBooleanField()
    sa = models.NullBooleanField()
    su = models.NullBooleanField()
    month_by = models.CharField(max_length=-1, blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    week_list = models.CharField(max_length=-1, blank=True, null=True)
    byday = models.CharField(max_length=-1, blank=True, null=True)
    final_date = models.DateField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    active = models.NullBooleanField()
    message_last_post = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_event'


class CalendarEventResPartnerRel(models.Model):
    calendar_event = models.ForeignKey(CalendarEvent, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'calendar_event_res_partner_rel'
        unique_together = (('calendar_event', 'res_partner'),)


class CalendarEventType(models.Model):
    name = models.CharField(unique=True, max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_event_type'


class CashBoxIn(models.Model):
    name = models.CharField(max_length=-1)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    ref = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cash_box_in'


class CashBoxOut(models.Model):
    name = models.CharField(max_length=-1)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cash_box_out'


class ChangePasswordUser(models.Model):
    wizard = models.ForeignKey('ChangePasswordWizard', models.DO_NOTHING)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    user_login = models.CharField(max_length=-1, blank=True, null=True)
    new_passwd = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'change_password_user'


class ChangePasswordWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'change_password_wizard'


class ClassRoom(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    number = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class_room'


class DecimalPrecision(models.Model):
    name = models.CharField(unique=True, max_length=-1)
    digits = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'decimal_precision'


class DecimalPrecisionTest(models.Model):
    float = models.FloatField(blank=True, null=True)
    float_2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    float_4 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'decimal_precision_test'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DocumentType(models.Model):
    seq_no = models.CharField(max_length=-1, blank=True, null=True)
    doc_type = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'document_type'


class ElectiveSubjectStudentRel(models.Model):
    subject = models.ForeignKey('SubjectSubject', models.DO_NOTHING)
    student = models.ForeignKey('StudentStudent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'elective_subject_student_rel'
        unique_together = (('subject', 'student'),)


class EmailTemplateAttachmentRel(models.Model):
    email_template = models.ForeignKey('MailTemplate', models.DO_NOTHING)
    attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'email_template_attachment_rel'
        unique_together = (('email_template', 'attachment'),)


class EmailTemplatePreview(models.Model):
    res_id = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    model_0 = models.CharField(db_column='model', max_length=-1, blank=True, null=True)  # Field renamed because of name conflict.
    lang = models.CharField(max_length=-1, blank=True, null=True)
    user_signature = models.NullBooleanField()
    subject = models.CharField(max_length=-1, blank=True, null=True)
    email_from = models.CharField(max_length=-1, blank=True, null=True)
    use_default_to = models.NullBooleanField()
    email_to = models.CharField(max_length=-1, blank=True, null=True)
    partner_to = models.CharField(max_length=-1, blank=True, null=True)
    email_cc = models.CharField(max_length=-1, blank=True, null=True)
    reply_to = models.CharField(max_length=-1, blank=True, null=True)
    mail_server = models.ForeignKey('IrMailServer', models.DO_NOTHING, blank=True, null=True)
    body_html = models.TextField(blank=True, null=True)
    report_name = models.CharField(max_length=-1, blank=True, null=True)
    report_template = models.ForeignKey('IrActReportXml', models.DO_NOTHING, db_column='report_template', blank=True, null=True)
    ref_ir_act_window = models.ForeignKey('IrActWindow', models.DO_NOTHING, db_column='ref_ir_act_window', blank=True, null=True)
    auto_delete = models.NullBooleanField()
    model_object_field = models.ForeignKey('IrModelFields', models.DO_NOTHING, db_column='model_object_field', blank=True, null=True)
    sub_object = models.ForeignKey('IrModel', models.DO_NOTHING, db_column='sub_object', blank=True, null=True)
    sub_model_object_field = models.ForeignKey('IrModelFields', models.DO_NOTHING, db_column='sub_model_object_field', blank=True, null=True)
    null_value = models.CharField(max_length=-1, blank=True, null=True)
    copyvalue = models.CharField(max_length=-1, blank=True, null=True)
    scheduled_date = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_template_preview'


class EmailTemplatePreviewResPartnerRel(models.Model):
    email_template_preview = models.ForeignKey(EmailTemplatePreview, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'email_template_preview_res_partner_rel'
        unique_together = (('email_template_preview', 'res_partner'),)


class EmployeeCategoryRel(models.Model):
    category = models.ForeignKey('HrEmployeeCategory', models.DO_NOTHING)
    emp = models.ForeignKey('HrEmployee', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'employee_category_rel'
        unique_together = (('category', 'emp'),)


class FeesStructurePayslipRel(models.Model):
    fees = models.ForeignKey('StudentFeesStructure', models.DO_NOTHING)
    slip = models.ForeignKey('StudentFeesStructureLine', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'fees_structure_payslip_rel'
        unique_together = (('fees', 'slip'),)


class FetchmailServer(models.Model):
    name = models.CharField(max_length=-1)
    active = models.NullBooleanField()
    state = models.CharField(max_length=-1, blank=True, null=True)
    server = models.CharField(max_length=-1, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=-1)
    is_ssl = models.NullBooleanField()
    attach = models.NullBooleanField()
    original = models.NullBooleanField()
    date = models.DateTimeField(blank=True, null=True)
    user = models.CharField(max_length=-1, blank=True, null=True)
    password = models.CharField(max_length=-1, blank=True, null=True)
    action = models.ForeignKey('IrActServer', models.DO_NOTHING, blank=True, null=True)
    object = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    configuration = models.TextField(blank=True, null=True)
    script = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fetchmail_server'


class FineTypes(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fine_types'


class GradeLine(models.Model):
    from_mark = models.IntegerField()
    to_mark = models.IntegerField()
    grade = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    fail = models.NullBooleanField()
    grade_0 = models.ForeignKey('GradeMaster', models.DO_NOTHING, db_column='grade_id', blank=True, null=True)  # Field renamed because of name conflict.
    name = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grade_line'


class GradeMaster(models.Model):
    name = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grade_master'


class HrDepartment(models.Model):
    name = models.CharField(max_length=-1)
    complete_name = models.CharField(max_length=-1, blank=True, null=True)
    active = models.NullBooleanField()
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    manager = models.ForeignKey('HrEmployee', models.DO_NOTHING, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_department'


class HrEmployee(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    active = models.NullBooleanField()
    address_home = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True)
    gender = models.CharField(max_length=-1, blank=True, null=True)
    marital = models.CharField(max_length=-1, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    ssnid = models.CharField(max_length=-1, blank=True, null=True)
    sinid = models.CharField(max_length=-1, blank=True, null=True)
    identification_id = models.CharField(max_length=-1, blank=True, null=True)
    passport_id = models.CharField(max_length=-1, blank=True, null=True)
    bank_account = models.ForeignKey('ResPartnerBank', models.DO_NOTHING, blank=True, null=True)
    permit_no = models.CharField(max_length=-1, blank=True, null=True)
    visa_no = models.CharField(max_length=-1, blank=True, null=True)
    visa_expire = models.DateField(blank=True, null=True)
    address = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    work_phone = models.CharField(max_length=-1, blank=True, null=True)
    mobile_phone = models.CharField(max_length=-1, blank=True, null=True)
    work_email = models.CharField(max_length=-1, blank=True, null=True)
    work_location = models.CharField(max_length=-1, blank=True, null=True)
    job = models.ForeignKey('HrJob', models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey(HrDepartment, models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    coach = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    resource = models.ForeignKey('ResourceResource', models.DO_NOTHING)
    message_last_post = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_employee'


class HrEmployeeCategory(models.Model):
    name = models.CharField(unique=True, max_length=-1)
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_employee_category'


class HrHolidays(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    payslip_status = models.NullBooleanField()
    report_note = models.TextField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    date_from = models.DateTimeField(blank=True, null=True)
    date_to = models.DateTimeField(blank=True, null=True)
    holiday_status = models.ForeignKey('HrHolidaysStatus', models.DO_NOTHING)
    employee = models.ForeignKey(HrEmployee, models.DO_NOTHING, blank=True, null=True)
    manager = models.ForeignKey(HrEmployee, models.DO_NOTHING, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    number_of_days_temp = models.FloatField(blank=True, null=True)
    number_of_days = models.FloatField(blank=True, null=True)
    meeting = models.ForeignKey(CalendarEvent, models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=-1)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey(HrDepartment, models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey(HrEmployeeCategory, models.DO_NOTHING, blank=True, null=True)
    holiday_type = models.CharField(max_length=-1)
    first_approver = models.ForeignKey(HrEmployee, models.DO_NOTHING, blank=True, null=True)
    second_approver = models.ForeignKey(HrEmployee, models.DO_NOTHING, blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_holidays'


class HrHolidaysStatus(models.Model):
    name = models.CharField(max_length=-1)
    categ = models.ForeignKey(CalendarEventType, models.DO_NOTHING, blank=True, null=True)
    color_name = models.CharField(max_length=-1)
    limit = models.NullBooleanField()
    active = models.NullBooleanField()
    double_validation = models.NullBooleanField()
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_holidays_status'


class HrHolidaysSummaryDept(models.Model):
    date_from = models.DateField()
    holiday_type = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_holidays_summary_dept'


class HrHolidaysSummaryEmployee(models.Model):
    date_from = models.DateField()
    holiday_type = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_holidays_summary_employee'


class HrJob(models.Model):
    name = models.CharField(max_length=-1)
    expected_employees = models.IntegerField(blank=True, null=True)
    no_of_employee = models.IntegerField(blank=True, null=True)
    no_of_recruitment = models.IntegerField(blank=True, null=True)
    no_of_hired_employee = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)
    department = models.ForeignKey(HrDepartment, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=-1)
    message_last_post = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_job'
        unique_together = (('name', 'company', 'department'),)


class IapAccount(models.Model):
    service_name = models.CharField(max_length=-1, blank=True, null=True)
    account_token = models.CharField(max_length=-1, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iap_account'


class IrActClient(models.Model):
    name = models.CharField(max_length=-1)
    type = models.CharField(max_length=-1)
    help = models.TextField(blank=True, null=True)
    binding_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    binding_type = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    tag = models.CharField(max_length=-1)
    target = models.CharField(max_length=-1, blank=True, null=True)
    res_model = models.CharField(max_length=-1, blank=True, null=True)
    context = models.CharField(max_length=-1)
    params_store = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_act_client'


class IrActReportXml(models.Model):
    name = models.CharField(max_length=-1)
    type = models.CharField(max_length=-1)
    help = models.TextField(blank=True, null=True)
    binding_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    binding_type = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    model = models.CharField(max_length=-1)
    report_type = models.CharField(max_length=-1)
    report_name = models.CharField(max_length=-1)
    report_file = models.CharField(max_length=-1, blank=True, null=True)
    multi = models.NullBooleanField()
    paperformat = models.ForeignKey('ReportPaperformat', models.DO_NOTHING, blank=True, null=True)
    print_report_name = models.CharField(max_length=-1, blank=True, null=True)
    attachment_use = models.NullBooleanField()
    attachment = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_act_report_xml'


class IrActServer(models.Model):
    name = models.CharField(max_length=-1)
    type = models.CharField(max_length=-1)
    help = models.TextField(blank=True, null=True)
    binding_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    binding_type = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    usage = models.CharField(max_length=-1)
    state = models.CharField(max_length=-1)
    sequence = models.IntegerField(blank=True, null=True)
    model = models.ForeignKey('IrModel', models.DO_NOTHING)
    model_name = models.CharField(max_length=-1, blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    crud_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    link_field = models.ForeignKey('IrModelFields', models.DO_NOTHING, blank=True, null=True)
    template = models.ForeignKey('MailTemplate', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_act_server'


class IrActServerMailChannelRel(models.Model):
    ir_act_server = models.ForeignKey(IrActServer, models.DO_NOTHING)
    mail_channel = models.ForeignKey('MailChannel', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ir_act_server_mail_channel_rel'
        unique_together = (('ir_act_server', 'mail_channel'),)


class IrActServerResPartnerRel(models.Model):
    ir_act_server = models.ForeignKey(IrActServer, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ir_act_server_res_partner_rel'
        unique_together = (('ir_act_server', 'res_partner'),)


class IrActUrl(models.Model):
    name = models.CharField(max_length=-1)
    type = models.CharField(max_length=-1)
    help = models.TextField(blank=True, null=True)
    binding_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    binding_type = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    url = models.TextField()
    target = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ir_act_url'


class IrActWindow(models.Model):
    name = models.CharField(max_length=-1)
    type = models.CharField(max_length=-1)
    help = models.TextField(blank=True, null=True)
    binding_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    binding_type = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    view = models.ForeignKey('IrUiView', models.DO_NOTHING, blank=True, null=True)
    domain = models.CharField(max_length=-1, blank=True, null=True)
    context = models.CharField(max_length=-1)
    res_id = models.IntegerField(blank=True, null=True)
    res_model = models.CharField(max_length=-1)
    src_model = models.CharField(max_length=-1, blank=True, null=True)
    target = models.CharField(max_length=-1, blank=True, null=True)
    view_mode = models.CharField(max_length=-1)
    view_type = models.CharField(max_length=-1)
    usage = models.CharField(max_length=-1, blank=True, null=True)
    limit = models.IntegerField(blank=True, null=True)
    search_view = models.ForeignKey('IrUiView', models.DO_NOTHING, blank=True, null=True)
    filter = models.NullBooleanField()
    auto_search = models.NullBooleanField()
    multi = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'ir_act_window'


class IrActWindowGroupRel(models.Model):
    act = models.ForeignKey(IrActWindow, models.DO_NOTHING)
    gid = models.ForeignKey('ResGroups', models.DO_NOTHING, db_column='gid')

    class Meta:
        managed = False
        db_table = 'ir_act_window_group_rel'
        unique_together = (('act', 'gid'),)


class IrActWindowView(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    view = models.ForeignKey('IrUiView', models.DO_NOTHING, blank=True, null=True)
    view_mode = models.CharField(max_length=-1)
    act_window = models.ForeignKey(IrActWindow, models.DO_NOTHING, blank=True, null=True)
    multi = models.NullBooleanField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_act_window_view'
        unique_together = (('act_window', 'view_mode'),)


class IrActions(models.Model):
    name = models.CharField(max_length=-1)
    type = models.CharField(max_length=-1)
    help = models.TextField(blank=True, null=True)
    binding_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    binding_type = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_actions'


class IrActionsTodo(models.Model):
    action_id = models.IntegerField()
    sequence = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_actions_todo'


class IrAttachment(models.Model):
    name = models.CharField(max_length=-1)
    datas_fname = models.CharField(max_length=-1, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    res_name = models.CharField(max_length=-1, blank=True, null=True)
    res_model = models.CharField(max_length=-1, blank=True, null=True)
    res_field = models.CharField(max_length=-1, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=-1)
    url = models.CharField(max_length=1024, blank=True, null=True)
    public = models.NullBooleanField()
    access_token = models.CharField(max_length=-1, blank=True, null=True)
    db_datas = models.BinaryField(blank=True, null=True)
    store_fname = models.CharField(max_length=-1, blank=True, null=True)
    file_size = models.IntegerField(blank=True, null=True)
    checksum = models.CharField(max_length=40, blank=True, null=True)
    mimetype = models.CharField(max_length=-1, blank=True, null=True)
    index_content = models.TextField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_attachment'


class IrConfigParameter(models.Model):
    key = models.CharField(unique=True, max_length=-1)
    value = models.TextField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_config_parameter'


class IrCron(models.Model):
    ir_actions_server = models.ForeignKey(IrActServer, models.DO_NOTHING)
    cron_name = models.CharField(max_length=-1, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    active = models.NullBooleanField()
    interval_number = models.IntegerField(blank=True, null=True)
    interval_type = models.CharField(max_length=-1, blank=True, null=True)
    numbercall = models.IntegerField(blank=True, null=True)
    doall = models.NullBooleanField()
    nextcall = models.DateTimeField()
    priority = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_cron'


class IrDefault(models.Model):
    field = models.ForeignKey('IrModelFields', models.DO_NOTHING)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    condition = models.CharField(max_length=-1, blank=True, null=True)
    json_value = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_default'


class IrExports(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    resource = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_exports'


class IrExportsLine(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    export = models.ForeignKey(IrExports, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_exports_line'


class IrFilters(models.Model):
    name = models.CharField(max_length=-1)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    domain = models.TextField()
    context = models.TextField()
    sort = models.TextField()
    model_id = models.CharField(max_length=-1)
    is_default = models.NullBooleanField()
    action_id = models.IntegerField(blank=True, null=True)
    active = models.NullBooleanField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
