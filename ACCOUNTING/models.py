# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models




class AccountInvoice(models.Model):
    name = models.CharField(max_length=1, blank=True, null=True)
    origin = models.CharField(max_length=1, blank=True, null=True)
    type = models.CharField(max_length=1, blank=True, null=True)
    access_token = models.CharField(max_length=1, blank=True, null=True)
    refund_invoice = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    number = models.CharField(max_length=1, blank=True, null=True)
    move_name = models.CharField(max_length=1, blank=True, null=True)
    reference = models.CharField(max_length=1, blank=True, null=True)
    reference_type = models.CharField(max_length=1)
    comment = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=1, blank=True, null=True)
    sent = models.NullBooleanField()
    date_invoice = models.DateField(blank=True, null=True)
    date_due = models.DateField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    #payment_term = models.ForeignKey('AccountPaymentTerm', models.DO_NOTHING, blank=True, null=True)
    #date = models.DateField(blank=True, null=True)
    #account = models.ForeignKey('AccountAccount', models.DO_NOTHING)
    #move = models.ForeignKey('AccountMove', models.DO_NOTHING, blank=True, null=True)
    #amount_untaxed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #amount_untaxed_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #amount_tax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #amount_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #amount_total_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #amount_total_company_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    #journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    #reconciled = models.NullBooleanField()
    #partner_bank = models.ForeignKey('ResPartnerBank', models.DO_NOTHING, blank=True, null=True)
    #residual = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #residual_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #residual_company_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    #fiscal_position = models.ForeignKey('AccountFiscalPosition', models.DO_NOTHING, blank=True, null=True)
    #commercial_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    #cash_rounding = models.ForeignKey('AccountCashRounding', models.DO_NOTHING, blank=True, null=True)
    #message_last_post = models.DateTimeField(blank=True, null=True)
    #activity_date_deadline = models.DateField(blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)
    #slip_ref = models.CharField(max_length=1, blank=True, null=True)
    #student_payslip = models.ForeignKey('StudentPayslip', models.DO_NOTHING, blank=True, null=True)
    #student_bulk_payslip = models.ForeignKey('StudentFeesRegister', models.DO_NOTHING, blank=True, null=True)
    #student_fine = models.FloatField(blank=True, null=True)
    #fine_type = models.ForeignKey('LateFeesRule', models.DO_NOTHING, blank=True, null=True)
    #fine_type_0 = models.CharField(db_column='fine_type', max_length=1, blank=True, null=True)  # Field renamed because of name conflict.
    #fine_rate = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #amount_fine = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #due_date_reminder = models.NullBooleanField()
    #fine_apply_flag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_invoice'
        unique_together = (('number', 'type'),)


#class ResUsers(models.Model):
    #active = models.NullBooleanField()
    #login = models.CharField(unique=True,max_length=1)
    #password = models.CharField(max_length=1, blank=True, null=True)
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    #partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    #signature = models.TextField(blank=True, null=True)
    #action_id = models.IntegerField(blank=True, null=True)
    #share = models.NullBooleanField()
    #create_uid = models.ForeignKey('self', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('self', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)
    #password_crypt = models.CharField(max_length=1, blank=True, null=True)
    #alias = models.ForeignKey('MailAlias', models.DO_NOTHING, blank=True, null=True)
    #notification_type = models.CharField(max_length=1)

    #class Meta:
        #managed = False
        #db_table = 'res_users'




#class MailAlias(models.Model):
    #alias_name = models.CharField(unique=True, max_length=1, blank=True, null=True)
    #alias_model = models.ForeignKey('IrModel', models.DO_NOTHING)
    #alias_user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    #alias_defaults = models.TextField()
    #alias_force_thread_id = models.IntegerField(blank=True, null=True)
    #alias_parent_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    #alias_parent_thread_id = models.IntegerField(blank=True, null=True)
    #alias_contact = models.CharField(max_length=1)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'mail_alias'




#class IrModel(models.Model):
    #name = models.CharField(max_length=1)
    #model = models.CharField(unique=True, max_length=1)
    #info = models.TextField(blank=True, null=True)
    #state = models.CharField(max_length=1, blank=True, null=True)
    #transient = models.NullBooleanField()
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)
    #is_mail_thread = models.NullBooleanField()

    #class Meta:
        #managed = False
        #db_table = 'ir_model'




class ResPartner(models.Model):
    name = models.CharField(max_length=1, blank=True, null=True)
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    #display_name = models.CharField(max_length=1, blank=True, null=True)
    #date = models.DateField(blank=True, null=True)
    #title = models.ForeignKey('ResPartnerTitle', models.DO_NOTHING, db_column='title', blank=True, null=True)
    #parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    #ref = models.CharField(max_length=1, blank=True, null=True)
    #lang = models.CharField(max_length=1, blank=True, null=True)
    #tz = models.CharField(max_length=1, blank=True, null=True)
    #user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    #vat = models.CharField(max_length=1, blank=True, null=True)
    #website = models.CharField(max_length=1, blank=True, null=True)
    #comment = models.TextField(blank=True, null=True)
    #credit_limit = models.FloatField(blank=True, null=True)
    #barcode = models.CharField(max_length=1, blank=True, null=True)
    #active = models.NullBooleanField()
    #customer = models.NullBooleanField()
    #supplier = models.NullBooleanField()
    #employee = models.NullBooleanField()
    #function = models.CharField(max_length=1, blank=True, null=True)
    #type = models.CharField(max_length=1, blank=True, null=True)
    #street = models.CharField(max_length=1, blank=True, null=True)
    #street2 = models.CharField(max_length=1, blank=True, null=True)
    #zip = models.CharField(max_length=1, blank=True, null=True)
    #city = models.CharField(max_length=1, blank=True, null=True)
    #state = models.ForeignKey('ResCountryState', models.DO_NOTHING, blank=True, null=True)
    #country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True)
    #email = models.CharField(max_length=1, blank=True, null=True)
    #phone = models.CharField(max_length=1, blank=True, null=True)
    #mobile = models.CharField(max_length=1, blank=True, null=True)
    #is_company = models.NullBooleanField()
    #industry = models.ForeignKey('ResPartnerIndustry', models.DO_NOTHING, blank=True, null=True)
    #color = models.IntegerField(blank=True, null=True)
    #partner_share = models.NullBooleanField()
    #commercial_partner = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    #commercial_partner_country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True)
    #commercial_company_name = models.CharField(max_length=1, blank=True, null=True)
    #company_name = models.CharField(max_length=1, blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)
    #activity_date_deadline = models.DateField(blank=True, null=True)
    #message_last_post = models.DateTimeField(blank=True, null=True)
    #message_bounce = models.IntegerField(blank=True, null=True)
    #opt_out = models.NullBooleanField()
    #signup_token = models.CharField(max_length=1, blank=True, null=True)
    #signup_type = models.CharField(max_length=1, blank=True, null=True)
    #signup_expiration = models.DateTimeField(blank=True, null=True)
    #debit_limit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #last_time_entries_checked = models.DateTimeField(blank=True, null=True)
    #invoice_warn = models.CharField(max_length=1)
    #invoice_warn_msg = models.TextField(blank=True, null=True)
    #picking_warn = models.CharField(max_length=1)
    #picking_warn_msg = models.TextField(blank=True, null=True)
    #calendar_last_notif_ack = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner'






#class ResPartnerIndustry(models.Model):
    #name = models.CharField(max_length=1, blank=True, null=True)
    #full_name = models.CharField(max_length=1, blank=True, null=True)
    #active = models.NullBooleanField()
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'res_partner_industry'










#class ResPartnerTitle(models.Model):
    #name = models.CharField(max_length=1)
    #shortcut = models.CharField(max_length=1, blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'res_partner_title'



#class ResCountryState(models.Model):
    #country = models.ForeignKey('ResCountry', models.DO_NOTHING)
    #name = models.CharField(max_length=1)
    #code = models.CharField(max_length=1)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)
    #l10n_in_tin = models.CharField(max_length=2, blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'res_country_state'
        #unique_together = (('country', 'code'),)








#class AccountPaymentTerm(models.Model):
    #name = models.CharField(max_length=1)
    #active = models.NullBooleanField()
    #note = models.TextField(blank=True, null=True)
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    #sequence = models.IntegerField()
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'account_payment_term'
        
        

#class AccountMove(models.Model):
    #name = models.CharField(max_length=1)
    #ref = models.CharField(max_length=1, blank=True, null=True)
    #date = models.DateField()
    #journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)
    #currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    #state = models.CharField(max_length=1)
    #partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    #amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #narration = models.TextField(blank=True, null=True)
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    #matched_percentage = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #tax_cash_basis_rec = models.ForeignKey('AccountPartialReconcile', models.DO_NOTHING, blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)
    #stock_move = models.ForeignKey('StockMove', models.DO_NOTHING, blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'account_move'




#class AccountPartialReconcile(models.Model):
    #debit_move = models.ForeignKey('AccountMoveLine', models.DO_NOTHING)
    #credit_move = models.ForeignKey('AccountMoveLine', models.DO_NOTHING)
    #amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    #full_reconcile = models.ForeignKey('AccountFullReconcile', models.DO_NOTHING, blank=True, null=True)
    #max_date = models.DateField(blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'account_partial_reconcile'




#class AccountFullReconcile(models.Model):
    #name = models.CharField(max_length=1)
    #exchange_move = models.ForeignKey('AccountMove', models.DO_NOTHING, blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'account_full_reconcile'




#class ProductUom(models.Model):
    #name = models.CharField(max_length=1)
    #category = models.ForeignKey('ProductUomCateg', models.DO_NOTHING)
    #factor = models.DecimalField(max_digits=65535, decimal_places=65535)
    #rounding = models.DecimalField(max_digits=65535, decimal_places=65535)
    #active = models.NullBooleanField()
    #uom_type = models.CharField(max_length=1)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'product_uom'



#class ProductUomCateg(models.Model):
    #name = models.CharField(max_length=1)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'product_uom_categ'



#class ProductProduct(models.Model):
    #default_code = models.CharField(max_length=1, blank=True, null=True)
    #active = models.NullBooleanField()
    #product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING)
    #barcode = models.CharField(unique=True, max_length=1, blank=True, null=True)
    #volume = models.FloatField(blank=True, null=True)
    #weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #message_last_post = models.DateTimeField(blank=True, null=True)
    #activity_date_deadline = models.DateField(blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'product_product'



#class ProductCategory(models.Model):
    #parent_left = models.IntegerField(blank=True, null=True)
    #parent_right = models.IntegerField(blank=True, null=True)
    #name = models.CharField(max_length=1)
    #complete_name = models.CharField(max_length=1, blank=True, null=True)
    #parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)
    #removal_strategy = models.ForeignKey('ProductRemoval', models.DO_NOTHING, blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'product_category'





#class ProductRemoval(models.Model):
    #name = models.CharField(max_length=1)
    #method = models.CharField(max_length=1)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'product_removal'


#class ProductTemplate(models.Model):
    #name = models.CharField(max_length=1)
    #sequence = models.IntegerField(blank=True, null=True)
    #description = models.TextField(blank=True, null=True)
    #description_purchase = models.TextField(blank=True, null=True)
    #description_sale = models.TextField(blank=True, null=True)
    #type = models.CharField(max_length=1)
    #rental = models.NullBooleanField()
    #categ = models.ForeignKey('ProductCategory', models.DO_NOTHING)
    #list_price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #volume = models.FloatField(blank=True, null=True)
    #weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #sale_ok = models.NullBooleanField()
    #purchase_ok = models.NullBooleanField()
    #uom = models.ForeignKey('ProductUom', models.DO_NOTHING)
    #uom_po = models.ForeignKey('ProductUom', models.DO_NOTHING)
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    #active = models.NullBooleanField()
    #color = models.IntegerField(blank=True, null=True)
    #default_code = models.CharField(max_length=1, blank=True, null=True)
    #message_last_post = models.DateTimeField(blank=True, null=True)
    #activity_date_deadline = models.DateField(blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)
    #l10n_in_hsn_code = models.CharField(max_length=1, blank=True, null=True)
    #service_type = models.CharField(max_length=1, blank=True, null=True)
    #sale_line_warn = models.CharField(max_length=1)
    #sale_line_warn_msg = models.TextField(blank=True, null=True)
    #expense_policy = models.CharField(max_length=1, blank=True, null=True)
    #invoice_policy = models.CharField(max_length=1, blank=True, null=True)
    #responsible = models.ForeignKey('ResUsers', models.DO_NOTHING)
    #sale_delay = models.FloatField(blank=True, null=True)
    #tracking = models.CharField(max_length=1)
    #description_picking = models.TextField(blank=True, null=True)
    #description_pickingout = models.TextField(blank=True, null=True)
    #description_pickingin = models.TextField(blank=True, null=True)
    #website_description = models.TextField(blank=True, null=True)
    #rating_last_value = models.FloatField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'product_template'



#class AccountPaymentMethod(models.Model):
    #name = models.CharField(max_length=1)
    #code = models.CharField(max_length=1)
    #payment_type = models.CharField(max_length=1)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'account_payment_method'


#class PaymentTransaction(models.Model):
    #create_date = models.DateTimeField(blank=True, null=True)
    #date_validate = models.DateTimeField(blank=True, null=True)
    #acquirer = models.ForeignKey('PaymentAcquirer', models.DO_NOTHING)
    #type = models.CharField(max_length=1)
    #state = models.CharField(max_length=1)
    #state_message = models.TextField(blank=True, null=True)
    #amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    #fees = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    #reference = models.CharField(max_length=1)
    #acquirer_reference = models.CharField(max_length=1, blank=True, null=True)
    #partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    #partner_name = models.CharField(max_length=1, blank=True, null=True)
    #partner_lang = models.CharField(max_length=1, blank=True, null=True)
    #partner_email = models.CharField(max_length=1, blank=True, null=True)
    #partner_zip = models.CharField(max_length=1, blank=True, null=True)
    #partner_address = models.CharField(max_length=1, blank=True, null=True)
    #partner_city = models.CharField(max_length=1, blank=True, null=True)
    #partner_country = models.ForeignKey('ResCountry', models.DO_NOTHING)
    #partner_phone = models.CharField(max_length=1, blank=True, null=True)
    #html_3ds = models.CharField(max_length=1, blank=True, null=True)
    #callback_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    #callback_res_id = models.IntegerField(blank=True, null=True)
    #callback_method = models.CharField(max_length=1, blank=True, null=True)
    #callback_hash = models.CharField(max_length=1, blank=True, null=True)
    #payment_token = models.ForeignKey('PaymentToken', models.DO_NOTHING, blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)
    #sale_order = models.ForeignKey('SaleOrder', models.DO_NOTHING, blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'payment_transaction'


#class IrModel(models.Model):
    #name = models.CharField(max_length=1)
    #model = models.CharField(unique=True, max_length=1)
    #info = models.TextField(blank=True, null=True)
    #state = models.CharField(max_length=1, blank=True, null=True)
    #transient = models.NullBooleanField()
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)
    #is_mail_thread = models.NullBooleanField()
    #website_form_access = models.NullBooleanField()
    #website_form_default_field_id = models.IntegerField(blank=True, null=True)
    #website_form_label = models.CharField(max_length=1, blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'ir_model'



#class PaymentAcquirer(models.Model):
    #name = models.CharField(max_length=1)
    #description = models.TextField(blank=True, null=True)
    #sequence = models.IntegerField(blank=True, null=True)
    #provider = models.CharField(max_length=1)
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    #view_template = models.ForeignKey('IrUiView', models.DO_NOTHING)
    #registration_view_template = models.ForeignKey('IrUiView', models.DO_NOTHING, blank=True, null=True)
    #environment = models.CharField(max_length=1)
    #website_published = models.NullBooleanField()
    #capture_manually = models.NullBooleanField()
    #journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True)
    #specific_countries = models.NullBooleanField()
    #pre_msg = models.TextField(blank=True, null=True)
    #post_msg = models.TextField(blank=True, null=True)
    #pending_msg = models.TextField(blank=True, null=True)
    #done_msg = models.TextField(blank=True, null=True)
    #cancel_msg = models.TextField(blank=True, null=True)
    #error_msg = models.TextField(blank=True, null=True)
    #save_token = models.CharField(max_length=1, blank=True, null=True)
    #fees_active = models.NullBooleanField()
    #fees_dom_fixed = models.FloatField(blank=True, null=True)
    #fees_dom_var = models.FloatField(blank=True, null=True)
    #fees_int_fixed = models.FloatField(blank=True, null=True)
    #fees_int_var = models.FloatField(blank=True, null=True)
    #module = models.ForeignKey('IrModuleModule', models.DO_NOTHING, blank=True, null=True)
    #payment_flow = models.CharField(max_length=1)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'payment_acquirer'


#class IrModuleModule(models.Model):
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #website = models.CharField(max_length=1, blank=True, null=True)
    #summary = models.CharField(max_length=1, blank=True, null=True)
    #name = models.CharField(unique=True, max_length=1)
    #author = models.CharField(max_length=1, blank=True, null=True)
    #icon = models.CharField(max_length=1, blank=True, null=True)
    #state = models.CharField(max_length=16, blank=True, null=True)
    #latest_version = models.CharField(max_length=1, blank=True, null=True)
    #shortdesc = models.CharField(max_length=1, blank=True, null=True)
    #category = models.ForeignKey('IrModuleCategory', models.DO_NOTHING, blank=True, null=True)
    #description = models.TextField(blank=True, null=True)
    #application = models.NullBooleanField()
    #demo = models.NullBooleanField()
    #web = models.NullBooleanField()
    #license = models.CharField(max_length=32, blank=True, null=True)
    #sequence = models.IntegerField(blank=True, null=True)
    #auto_install = models.NullBooleanField()
    #maintainer = models.CharField(max_length=1, blank=True, null=True)
    #contributors = models.TextField(blank=True, null=True)
    #published_version = models.CharField(max_length=1, blank=True, null=True)
    #url = models.CharField(max_length=1, blank=True, null=True)
    #menus_by_module = models.TextField(blank=True, null=True)
    #reports_by_module = models.TextField(blank=True, null=True)
    #views_by_module = models.TextField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'ir_module_module'




#class IrModuleCategory(models.Model):
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    #name = models.CharField(max_length=1)
    #description = models.TextField(blank=True, null=True)
    #sequence = models.IntegerField(blank=True, null=True)
    #visible = models.NullBooleanField()
    #exclusive = models.NullBooleanField()

    #class Meta:
        #managed = False
        #db_table = 'ir_module_category'





#class IrUiView(models.Model):
    #name = models.CharField(max_length=1)
    #model = models.CharField(max_length=1, blank=True, null=True)
    #key = models.CharField(max_length=1, blank=True, null=True)
    #priority = models.IntegerField()
    #type = models.CharField(max_length=1, blank=True, null=True)
    #arch_db = models.TextField(blank=True, null=True)
    #arch_fs = models.CharField(max_length=1, blank=True, null=True)
    #inherit = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    #field_parent = models.CharField(max_length=1, blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)
    #mode = models.CharField(max_length=1)
    #active = models.NullBooleanField()
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #website_meta_title = models.CharField(max_length=1, blank=True, null=True)
    #website_meta_description = models.TextField(blank=True, null=True)
    #website_meta_keywords = models.CharField(max_length=1, blank=True, null=True)
    #customize_show = models.NullBooleanField()
    #website_id = models.IntegerField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'ir_ui_view'




#class SaleOrder(models.Model):
    #name = models.CharField(max_length=1)
    #origin = models.CharField(max_length=1, blank=True, null=True)
    #client_order_ref = models.CharField(max_length=1, blank=True, null=True)
    #access_token = models.CharField(max_length=1, blank=True, null=True)
    #state = models.CharField(max_length=1, blank=True, null=True)
    #date_order = models.DateTimeField()
    #validity_date = models.DateField(blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #confirmation_date = models.DateTimeField(blank=True, null=True)
    #user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    #partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    #partner_invoice = models.ForeignKey('ResPartner', models.DO_NOTHING)
    #partner_shipping = models.ForeignKey('ResPartner', models.DO_NOTHING)
    #pricelist = models.ForeignKey('ProductPricelist', models.DO_NOTHING)
    #analytic_account = models.ForeignKey('AccountAnalyticAccount', models.DO_NOTHING, blank=True, null=True)
    #invoice_status = models.CharField(max_length=1, blank=True, null=True)
    #note = models.TextField(blank=True, null=True)
    #amount_untaxed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #amount_tax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #amount_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #payment_term = models.ForeignKey('AccountPaymentTerm', models.DO_NOTHING, blank=True, null=True)
    #fiscal_position = models.ForeignKey('AccountFiscalPosition', models.DO_NOTHING, blank=True, null=True)
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    #team = models.ForeignKey('CrmTeam', models.DO_NOTHING, blank=True, null=True)
    #message_last_post = models.DateTimeField(blank=True, null=True)
    #activity_date_deadline = models.DateField(blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)
    #payment_tx = models.ForeignKey('PaymentTransaction', models.DO_NOTHING, blank=True, null=True)
    #payment_acquirer = models.ForeignKey('PaymentAcquirer', models.DO_NOTHING, blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'sale_order'


#class ResCountryGroup(models.Model):
    #name = models.CharField(max_length=1)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'res_country_group'



#class AccountFiscalPosition(models.Model):
    #sequence = models.IntegerField(blank=True, null=True)
    #name = models.CharField(max_length=1)
    #active = models.NullBooleanField()
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    #note = models.TextField(blank=True, null=True)
    #auto_apply = models.NullBooleanField()
    #vat_required = models.NullBooleanField()
    #country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True)
    #country_group = models.ForeignKey('ResCountryGroup', models.DO_NOTHING, blank=True, null=True)
    #zip_from = models.IntegerField(blank=True, null=True)
    #zip_to = models.IntegerField(blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'account_fiscal_position'







#class AccountAnalyticAccount(models.Model):
    #name = models.CharField(max_length=1)
    #code = models.CharField(max_length=1, blank=True, null=True)
    #active = models.NullBooleanField()
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    #partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    #message_last_post = models.DateTimeField(blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'account_analytic_account'


#class ProductPricelist(models.Model):
    #name = models.CharField(max_length=1)
    #active = models.NullBooleanField()
    #currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    #sequence = models.IntegerField(blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)
    #discount_policy = models.CharField(max_length=1, blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'product_pricelist'






#class PaymentToken(models.Model):
    #name = models.CharField(max_length=1, blank=True, null=True)
    #partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    #acquirer = models.ForeignKey('PaymentAcquirer', models.DO_NOTHING)
    #acquirer_ref = models.CharField(max_length=1)
    #active = models.NullBooleanField()
    #verified = models.NullBooleanField()
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'payment_token'








#class AccountPayment(models.Model):
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    #name = models.CharField(max_length=1, blank=True, null=True)
    #state = models.CharField(max_length=1, blank=True, null=True)
    #payment_type = models.CharField(max_length=1)
    #payment_reference = models.CharField(max_length=1, blank=True, null=True)
    #move_name = models.CharField(max_length=1, blank=True, null=True)
    #destination_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True)
    #payment_difference_handling = models.CharField(max_length=1, blank=True, null=True)
    #writeoff_account = models.ForeignKey('AccountAccount', models.DO_NOTHING, blank=True, null=True)
    #writeoff_label = models.CharField(max_length=1, blank=True, null=True)
    #message_last_post = models.DateTimeField(blank=True, null=True)
    #payment_method = models.ForeignKey('AccountPaymentMethod', models.DO_NOTHING)
    #partner_type = models.CharField(max_length=1, blank=True, null=True)
    #partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    #amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    #currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    #payment_date = models.DateField()
    #communication = models.CharField(max_length=1, blank=True, null=True)
    #journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)
    #payment_transaction = models.ForeignKey('PaymentTransaction', models.DO_NOTHING, blank=True, null=True)
    #payment_token = models.ForeignKey('PaymentToken', models.DO_NOTHING, blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'account_payment'





#class AccountBankStatementLine(models.Model):
    #name = models.CharField(max_length=1)
    #date = models.DateField()
    #amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    #bank_account = models.ForeignKey('ResPartnerBank', models.DO_NOTHING, blank=True, null=True)
    #account = models.ForeignKey('AccountAccount', models.DO_NOTHING, blank=True, null=True)
    #statement = models.ForeignKey('AccountBankStatement', models.DO_NOTHING)
    #journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True)
    #partner_name = models.CharField(max_length=1, blank=True, null=True)
    #ref = models.CharField(max_length=1, blank=True, null=True)
    #note = models.TextField(blank=True, null=True)
    #sequence = models.IntegerField(blank=True, null=True)
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    #amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    #move_name = models.CharField(max_length=1, blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)
    #unique_import_id = models.CharField(unique=True, max_length=1, blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'account_bank_statement_line'




#class AccountBankStatement(models.Model):
    #message_last_post = models.DateTimeField(blank=True, null=True)
    #name = models.CharField(max_length=1, blank=True, null=True)
    #reference = models.CharField(max_length=1, blank=True, null=True)
    #date = models.DateField()
    #date_done = models.DateTimeField(blank=True, null=True)
    #balance_start = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #balance_end_real = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #state = models.CharField(max_length=1)
    #journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    #total_entry_encoding = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #balance_end = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #difference = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    #cashbox_start = models.ForeignKey('AccountBankStatementCashbox', models.DO_NOTHING, blank=True, null=True)
    #cashbox_end = models.ForeignKey('AccountBankStatementCashbox', models.DO_NOTHING, blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'account_bank_statement'


#class AccountBankStatementCashbox(models.Model):
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'account_bank_statement_cashbox'






#class AccountMoveLine(models.Model):
    #name = models.CharField(max_length=1, blank=True, null=True)
    #quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #product_uom = models.ForeignKey('ProductUom', models.DO_NOTHING, blank=True, null=True)
    #product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True)
    #debit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #credit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #balance = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #debit_cash_basis = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #credit_cash_basis = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #balance_cash_basis = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #company_currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    #currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    #amount_residual = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #amount_residual_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #tax_base_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #account = models.ForeignKey('AccountAccount', models.DO_NOTHING)
    #move = models.ForeignKey('AccountMove', models.DO_NOTHING)
    #ref = models.CharField(max_length=1, blank=True, null=True)
    #payment = models.ForeignKey('AccountPayment', models.DO_NOTHING, blank=True, null=True)
    #statement_line = models.ForeignKey('AccountBankStatementLine', models.DO_NOTHING, blank=True, null=True)
    #statement = models.ForeignKey('AccountBankStatement', models.DO_NOTHING, blank=True, null=True)
    #reconciled = models.NullBooleanField()
    #full_reconcile = models.ForeignKey('AccountFullReconcile', models.DO_NOTHING, blank=True, null=True)
    #journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True)
    #blocked = models.NullBooleanField()
    #date_maturity = models.DateField()
    #date = models.DateField(blank=True, null=True)
    #tax_line = models.ForeignKey('AccountTax', models.DO_NOTHING, blank=True, null=True)
    #analytic_account = models.ForeignKey('AccountAnalyticAccount', models.DO_NOTHING, blank=True, null=True)
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    #invoice = models.ForeignKey('AccountInvoice', models.DO_NOTHING, blank=True, null=True)
    #partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    #user_type = models.ForeignKey('AccountAccountType', models.DO_NOTHING, blank=True, null=True)
    #tax_exigible = models.NullBooleanField()
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)
    #stored_invoice = models.ForeignKey('AccountInvoice', models.DO_NOTHING, blank=True, null=True)
    #invoice_user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'account_move_line'















#class ProductPackaging(models.Model):
    #name = models.CharField(max_length=1)
    #sequence = models.IntegerField(blank=True, null=True)
    #product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True)
    #qty = models.FloatField(blank=True, null=True)
    #barcode = models.CharField(max_length=1, blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'product_packaging'


#class ProductRemoval(models.Model):
    #name = models.CharField(max_length=1)
    #method = models.CharField(max_length=1)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'product_removal'



#class ProductPutaway(models.Model):
    #name = models.CharField(max_length=1)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'product_putaway'


#class ProcurementGroup(models.Model):
    #partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    #name = models.CharField(max_length=1)
    #move_type = models.CharField(max_length=1)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'procurement_group'

#class StockPickingType(models.Model):
    #name = models.CharField(max_length=1)
    #color = models.IntegerField(blank=True, null=True)
    #sequence = models.IntegerField(blank=True, null=True)
    #sequence_0 = models.ForeignKey('IrSequence', models.DO_NOTHING, db_column='sequence_id')  # Field renamed because of name conflict.
    #default_location_src = models.ForeignKey('StockLocation', models.DO_NOTHING, blank=True, null=True)
    #default_location_dest = models.ForeignKey('StockLocation', models.DO_NOTHING, blank=True, null=True)
    #code = models.CharField(max_length=1)
    #return_picking_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    #show_entire_packs = models.NullBooleanField()
    #warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    #active = models.NullBooleanField()
    #use_create_lots = models.NullBooleanField()
    #use_existing_lots = models.NullBooleanField()
    #show_operations = models.NullBooleanField()
    #show_reserved = models.NullBooleanField()
    #barcode_nomenclature = models.ForeignKey('BarcodeNomenclature', models.DO_NOTHING, blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'stock_picking_type'



#class BarcodeNomenclature(models.Model):
    #name = models.CharField(max_length=32)
    #upc_ean_conv = models.CharField(max_length=1)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'barcode_nomenclature'



#class StockWarehouse(models.Model):
    #name = models.CharField(max_length=1)
    #active = models.NullBooleanField()
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    #partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    #view_location = models.ForeignKey('StockLocation', models.DO_NOTHING)
    #lot_stock = models.ForeignKey('StockLocation', models.DO_NOTHING)
    #code = models.CharField(max_length=5)
    #reception_steps = models.CharField(max_length=1)
    #delivery_steps = models.CharField(max_length=1)
    #wh_input_stock_loc = models.ForeignKey('StockLocation', models.DO_NOTHING, blank=True, null=True)
    #wh_qc_stock_loc = models.ForeignKey('StockLocation', models.DO_NOTHING, blank=True, null=True)
    #wh_output_stock_loc = models.ForeignKey('StockLocation', models.DO_NOTHING, blank=True, null=True)
    #wh_pack_stock_loc = models.ForeignKey('StockLocation', models.DO_NOTHING, blank=True, null=True)
    #mto_pull = models.ForeignKey('ProcurementRule', models.DO_NOTHING, blank=True, null=True)
    #pick_type = models.ForeignKey('StockPickingType', models.DO_NOTHING, blank=True, null=True)
    #pack_type = models.ForeignKey('StockPickingType', models.DO_NOTHING, blank=True, null=True)
    #out_type = models.ForeignKey('StockPickingType', models.DO_NOTHING, blank=True, null=True)
    #in_type = models.ForeignKey('StockPickingType', models.DO_NOTHING, blank=True, null=True)
    #int_type = models.ForeignKey('StockPickingType', models.DO_NOTHING, blank=True, null=True)
    #crossdock_route = models.ForeignKey('StockLocationRoute', models.DO_NOTHING, blank=True, null=True)
    #reception_route = models.ForeignKey('StockLocationRoute', models.DO_NOTHING, blank=True, null=True)
    #delivery_route = models.ForeignKey('StockLocationRoute', models.DO_NOTHING, blank=True, null=True)
    #default_resupply_wh = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'stock_warehouse'
        #unique_together = (('code', 'company'), ('name', 'company'),)



#class StockLocationRoute(models.Model):
    #name = models.CharField(max_length=1)
    #active = models.NullBooleanField()
    #sequence = models.IntegerField(blank=True, null=True)
    #product_selectable = models.NullBooleanField()
    #product_categ_selectable = models.NullBooleanField()
    #warehouse_selectable = models.NullBooleanField()
    #supplied_wh = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    #supplier_wh = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'stock_location_route'


#class ProcurementRule(models.Model):
    #name = models.CharField(max_length=1)
    #active = models.NullBooleanField()
    #group_propagation_option = models.CharField(max_length=1, blank=True, null=True)
    #group = models.ForeignKey('ProcurementGroup', models.DO_NOTHING, blank=True, null=True)
    #action = models.CharField(max_length=1)
    #sequence = models.IntegerField(blank=True, null=True)
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    #location = models.ForeignKey('StockLocation', models.DO_NOTHING, blank=True, null=True)
    #location_src = models.ForeignKey('StockLocation', models.DO_NOTHING, blank=True, null=True)
    #route = models.ForeignKey('StockLocationRoute', models.DO_NOTHING)
    #procure_method = models.CharField(max_length=1)
    #route_sequence = models.IntegerField(blank=True, null=True)
    #picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING)
    #delay = models.IntegerField(blank=True, null=True)
    #partner_address = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    #propagate = models.NullBooleanField()
    #warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    #propagate_warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'procurement_rule'






#class IrSequence(models.Model):
    #name = models.CharField(max_length=1)
    #code = models.CharField(max_length=1, blank=True, null=True)
    #implementation = models.CharField(max_length=1)
    #active = models.NullBooleanField()
    #prefix = models.CharField(max_length=1, blank=True, null=True)
    #suffix = models.CharField(max_length=1, blank=True, null=True)
    #number_next = models.IntegerField()
    #number_increment = models.IntegerField()
    #padding = models.IntegerField()
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    #use_date_range = models.NullBooleanField()
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'ir_sequence'




#class StockPicking(models.Model):
    #name = models.CharField(max_length=1, blank=True, null=True)
    #origin = models.CharField(max_length=1, blank=True, null=True)
    #note = models.TextField(blank=True, null=True)
    #backorder = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    #move_type = models.CharField(max_length=1)
    #state = models.CharField(max_length=1, blank=True, null=True)
    #group = models.ForeignKey('ProcurementGroup', models.DO_NOTHING, blank=True, null=True)
    #priority = models.CharField(max_length=1, blank=True, null=True)
    #scheduled_date = models.DateTimeField(blank=True, null=True)
    #date = models.DateTimeField(blank=True, null=True)
    #date_done = models.DateTimeField(blank=True, null=True)
    #location = models.ForeignKey('StockLocation', models.DO_NOTHING)
    #location_dest = models.ForeignKey('StockLocation', models.DO_NOTHING)
    #picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING)
    #partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    #owner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    #printed = models.NullBooleanField()
    #is_locked = models.NullBooleanField()
    #message_last_post = models.DateTimeField(blank=True, null=True)
    #activity_date_deadline = models.DateField(blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'stock_picking'
        #unique_together = (('name', 'company'),)








#class StockLocation(models.Model):
    #parent_left = models.IntegerField(blank=True, null=True)
    #parent_right = models.IntegerField(blank=True, null=True)
    #name = models.CharField(max_length=1)
    #complete_name = models.CharField(max_length=1, blank=True, null=True)
    #active = models.NullBooleanField()
    #usage = models.CharField(max_length=1)
    #location = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    #partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    #comment = models.TextField(blank=True, null=True)
    #posx = models.IntegerField(blank=True, null=True)
    #posy = models.IntegerField(blank=True, null=True)
    #posz = models.IntegerField(blank=True, null=True)
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    #scrap_location = models.NullBooleanField()
    #return_location = models.NullBooleanField()
    #removal_strategy = models.ForeignKey('ProductRemoval', models.DO_NOTHING, blank=True, null=True)
    #putaway_strategy = models.ForeignKey('ProductPutaway', models.DO_NOTHING, blank=True, null=True)
    #barcode = models.CharField(max_length=1, blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)
    #valuation_in_account = models.ForeignKey('AccountAccount', models.DO_NOTHING, blank=True, null=True)
    #valuation_out_account = models.ForeignKey('AccountAccount', models.DO_NOTHING, blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'stock_location'
        #unique_together = (('barcode', 'company'),)



#class StockLocationPath(models.Model):
    #name = models.CharField(max_length=1)
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    #route = models.ForeignKey('StockLocationRoute', models.DO_NOTHING)
    #location_from = models.ForeignKey('StockLocation', models.DO_NOTHING)
    #location_dest = models.ForeignKey('StockLocation', models.DO_NOTHING)
    #delay = models.IntegerField(blank=True, null=True)
    #picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING)
    #auto = models.CharField(max_length=1)
    #propagate = models.NullBooleanField()
    #active = models.NullBooleanField()
    #warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    #route_sequence = models.IntegerField(blank=True, null=True)
    #sequence = models.IntegerField(blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'stock_location_path'



#class StockMove(models.Model):
    #name = models.CharField(max_length=1)
    #sequence = models.IntegerField(blank=True, null=True)
    #priority = models.CharField(max_length=1, blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #date = models.DateTimeField()
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    #date_expected = models.DateTimeField()
    #product = models.ForeignKey('ProductProduct', models.DO_NOTHING)
    #ordered_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #product_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #product_uom_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    #product_uom = models.ForeignKey('ProductUom', models.DO_NOTHING, db_column='product_uom')
    #product_packaging = models.ForeignKey('ProductPackaging', models.DO_NOTHING, db_column='product_packaging', blank=True, null=True)
    #location = models.ForeignKey('StockLocation', models.DO_NOTHING)
    #location_dest = models.ForeignKey('StockLocation', models.DO_NOTHING)
    #partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    #picking = models.ForeignKey('StockPicking', models.DO_NOTHING, blank=True, null=True)
    #note = models.TextField(blank=True, null=True)
    #state = models.CharField(max_length=1, blank=True, null=True)
    #price_unit = models.FloatField(blank=True, null=True)
    #origin = models.CharField(max_length=1, blank=True, null=True)
    #procure_method = models.CharField(max_length=1)
    #scrapped = models.NullBooleanField()
    #group = models.ForeignKey('ProcurementGroup', models.DO_NOTHING, blank=True, null=True)
    #rule = models.ForeignKey('ProcurementRule', models.DO_NOTHING, blank=True, null=True)
    #push_rule = models.ForeignKey('StockLocationPath', models.DO_NOTHING, blank=True, null=True)
    #propagate = models.NullBooleanField()
    #picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING, blank=True, null=True)
    #inventory = models.ForeignKey('StockInventory', models.DO_NOTHING, blank=True, null=True)
    #origin_returned_move = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    #restrict_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    #warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    #additional = models.NullBooleanField()
    #reference = models.CharField(max_length=1, blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)
    #to_refund = models.NullBooleanField()
    #value = models.FloatField(blank=True, null=True)
    #remaining_qty = models.FloatField(blank=True, null=True)
    #remaining_value = models.FloatField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'stock_move'



#class StockProductionLot(models.Model):
    #name = models.CharField(max_length=1)
    #ref = models.CharField(max_length=1, blank=True, null=True)
    #product = models.ForeignKey('ProductProduct', models.DO_NOTHING)
    #product_uom = models.ForeignKey('ProductUom', models.DO_NOTHING, blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #message_last_post = models.DateTimeField(blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'stock_production_lot'
        #unique_together = (('name', 'product'),)

#class StockInventory(models.Model):
    #name = models.CharField(max_length=1)
    #date = models.DateTimeField()
    #state = models.CharField(max_length=1, blank=True, null=True)
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    #location = models.ForeignKey('StockLocation', models.DO_NOTHING)
    #product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True)
    #package = models.ForeignKey('StockQuantPackage', models.DO_NOTHING, blank=True, null=True)
    #partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    #lot = models.ForeignKey('StockProductionLot', models.DO_NOTHING, blank=True, null=True)
    #filter = models.CharField(max_length=1)
    #category = models.ForeignKey('ProductCategory', models.DO_NOTHING, blank=True, null=True)
    #exhausted = models.NullBooleanField()
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)
    #accounting_date = models.DateField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'stock_inventory'

#class StockQuantPackage(models.Model):
    #name = models.CharField(max_length=1, blank=True, null=True)
    #packaging = models.ForeignKey('ProductPackaging', models.DO_NOTHING, blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'stock_quant_package'






#class AccountAccount(models.Model):
    #name = models.CharField(max_length=1)
    #currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    #code = models.CharField(max_length=64)
    #deprecated = models.NullBooleanField()
    #user_type = models.ForeignKey('AccountAccountType', models.DO_NOTHING)
    #internal_type = models.CharField(max_length=1, blank=True, null=True)
    #last_time_entries_checked = models.DateTimeField(blank=True, null=True)
    #reconcile = models.NullBooleanField()
    #note = models.TextField(blank=True, null=True)
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    #group = models.ForeignKey('AccountGroup', models.DO_NOTHING, blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'account_account'
        #unique_together = (('code', 'company'),)






#class AccountAccountType(models.Model):
    #name = models.CharField(max_length=1)
    #include_initial_balance = models.NullBooleanField()
    #type = models.CharField(max_length=1)
    #note = models.TextField(blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'account_account_type'





#class AccountGroup(models.Model):
    #parent_left = models.IntegerField(blank=True, null=True)
    #parent_right = models.IntegerField(blank=True, null=True)
    #parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    #name = models.CharField(max_length=1)
    #code_prefix = models.CharField(max_length=1, blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'account_group'











#class ResCurrency(models.Model):
    #name = models.CharField(unique=True, max_length=1)
    #symbol = models.CharField(max_length=1)
    #rounding = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #active = models.NullBooleanField()
    #position = models.CharField(max_length=1, blank=True, null=True)
    #currency_unit_label = models.CharField(max_length=1, blank=True, null=True)
    #currency_subunit_label = models.CharField(max_length=1, blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'res_currency'



#class AccountJournal(models.Model):
    #name = models.CharField(max_length=1)
    #code = models.CharField(max_length=5)
    #active = models.NullBooleanField()
    #type = models.CharField(max_length=1)
    #default_credit_account = models.ForeignKey('AccountAccount', models.DO_NOTHING, blank=True, null=True)
    #default_debit_account = models.ForeignKey('AccountAccount', models.DO_NOTHING, blank=True, null=True)
    #update_posted = models.NullBooleanField()
    #group_invoice_lines = models.NullBooleanField()
    #sequence = models.ForeignKey('IrSequence', models.DO_NOTHING)
    #refund_sequence = models.ForeignKey('IrSequence', models.DO_NOTHING, blank=True, null=True)
    #sequence_0 = models.IntegerField(db_column='sequence', blank=True, null=True)  # Field renamed because of name conflict.
    #currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    #refund_sequence_0 = models.NullBooleanField(db_column='refund_sequence')  # Field renamed because of name conflict.
    #at_least_one_inbound = models.NullBooleanField()
    #at_least_one_outbound = models.NullBooleanField()
    #profit_account = models.ForeignKey('AccountAccount', models.DO_NOTHING, blank=True, null=True)
    #loss_account = models.ForeignKey('AccountAccount', models.DO_NOTHING, blank=True, null=True)
    #bank_account = models.ForeignKey('ResPartnerBank', models.DO_NOTHING, blank=True, null=True)
    #bank_statements_source = models.CharField(max_length=1, blank=True, null=True)
    #show_on_dashboard = models.NullBooleanField()
    #color = models.IntegerField(blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'account_journal'
        #unique_together = (('code', 'name', 'company'),)



#class ReportPaperformat(models.Model):
    #name = models.CharField(max_length=1)
    #default = models.NullBooleanField()
    #format = models.CharField(max_length=1, blank=True, null=True)
    #margin_top = models.FloatField(blank=True, null=True)
    #margin_bottom = models.FloatField(blank=True, null=True)
    #margin_left = models.FloatField(blank=True, null=True)
    #margin_right = models.FloatField(blank=True, null=True)
    #page_height = models.IntegerField(blank=True, null=True)
    #page_width = models.IntegerField(blank=True, null=True)
    #orientation = models.CharField(max_length=1, blank=True, null=True)
    #header_line = models.NullBooleanField()
    #header_spacing = models.IntegerField(blank=True, null=True)
    #dpi = models.IntegerField()
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'report_paperformat'


#class ResourceCalendar(models.Model):
    #name = models.CharField(max_length=1)
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'resource_calendar'


#class ResCompany(models.Model):
    #name = models.CharField(unique=True, max_length=1)
    #partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    #currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    #sequence = models.IntegerField(blank=True, null=True)
    #parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    #report_header = models.TextField(blank=True, null=True)
    #report_footer = models.TextField(blank=True, null=True)
    #logo_web = models.BinaryField(blank=True, null=True)
    #account_no = models.CharField(max_length=1, blank=True, null=True)
    #email = models.CharField(max_length=1, blank=True, null=True)
    #phone = models.CharField(max_length=1, blank=True, null=True)
    #company_registry = models.CharField(max_length=1, blank=True, null=True)
    #paperformat = models.ForeignKey('ReportPaperformat', models.DO_NOTHING, blank=True, null=True)
    #external_report_layout = models.CharField(max_length=1, blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)
    #resource_calendar = models.ForeignKey('ResourceCalendar', models.DO_NOTHING, blank=True, null=True)
    #fiscalyear_last_day = models.IntegerField()
    #fiscalyear_last_month = models.IntegerField()
    #period_lock_date = models.DateField(blank=True, null=True)
    #fiscalyear_lock_date = models.DateField(blank=True, null=True)
    #transfer_account = models.ForeignKey('AccountAccount', models.DO_NOTHING, blank=True, null=True)
    #expects_chart_of_accounts = models.NullBooleanField()
    #chart_template = models.ForeignKey('AccountChartTemplate', models.DO_NOTHING, blank=True, null=True)
    #bank_account_code_prefix = models.CharField(max_length=1, blank=True, null=True)
    #cash_account_code_prefix = models.CharField(max_length=1, blank=True, null=True)
    #accounts_code_digits = models.IntegerField(blank=True, null=True)
    #tax_cash_basis_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True)
    #tax_calculation_rounding_method = models.CharField(max_length=1, blank=True, null=True)
    #currency_exchange_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True)
    #anglo_saxon_accounting = models.NullBooleanField()
    #property_stock_account_input_categ = models.ForeignKey('AccountAccount', models.DO_NOTHING, blank=True, null=True)
    #property_stock_account_output_categ = models.ForeignKey('AccountAccount', models.DO_NOTHING, blank=True, null=True)
    #property_stock_valuation_account = models.ForeignKey('AccountAccount', models.DO_NOTHING, blank=True, null=True)
    #overdue_msg = models.TextField(blank=True, null=True)
    #tax_exigibility = models.NullBooleanField()
    #account_opening_move = models.ForeignKey('AccountMove', models.DO_NOTHING, blank=True, null=True)
    #account_setup_company_data_done = models.NullBooleanField()
    #account_setup_bank_data_done = models.NullBooleanField()
    #account_setup_fy_data_done = models.NullBooleanField()
    #account_setup_coa_done = models.NullBooleanField()
    #account_setup_bar_closed = models.NullBooleanField()
    #propagation_minimum_delta = models.IntegerField(blank=True, null=True)
    #internal_transit_location = models.ForeignKey('StockLocation', models.DO_NOTHING, blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'res_company'

#class AccountAccountTemplate(models.Model):
    #name = models.CharField(max_length=-1)
    #currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    #code = models.CharField(max_length=64)
    #user_type = models.ForeignKey('AccountAccountType', models.DO_NOTHING)
    #reconcile = models.NullBooleanField()
    #note = models.TextField(blank=True, null=True)
    #nocreate = models.NullBooleanField()
    #chart_template = models.ForeignKey('AccountChartTemplate', models.DO_NOTHING, blank=True, null=True)
    #group = models.ForeignKey('AccountGroup', models.DO_NOTHING, blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'account_account_template'



#class AccountChartTemplate(models.Model):
    #name = models.CharField(max_length=1)
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    #parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    #code_digits = models.IntegerField()
    #visible = models.NullBooleanField()
    #currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    #use_anglo_saxon = models.NullBooleanField()
    #complete_tax_set = models.NullBooleanField()
    #bank_account_code_prefix = models.CharField(max_length=1, blank=True, null=True)
    #cash_account_code_prefix = models.CharField(max_length=1, blank=True, null=True)
    #transfer_account = models.ForeignKey('AccountAccountTemplate', models.DO_NOTHING)
    #income_currency_exchange_account = models.ForeignKey('AccountAccountTemplate', models.DO_NOTHING, blank=True, null=True)
    #expense_currency_exchange_account = models.ForeignKey('AccountAccountTemplate', models.DO_NOTHING, blank=True, null=True)
    #property_account_receivable = models.ForeignKey('AccountAccountTemplate', models.DO_NOTHING, blank=True, null=True)
    #property_account_payable = models.ForeignKey('AccountAccountTemplate', models.DO_NOTHING, blank=True, null=True)
    #property_account_expense_categ = models.ForeignKey('AccountAccountTemplate', models.DO_NOTHING, blank=True, null=True)
    #property_account_income_categ = models.ForeignKey('AccountAccountTemplate', models.DO_NOTHING, blank=True, null=True)
    #property_account_expense = models.ForeignKey('AccountAccountTemplate', models.DO_NOTHING, blank=True, null=True)
    #property_account_income = models.ForeignKey('AccountAccountTemplate', models.DO_NOTHING, blank=True, null=True)
    #property_stock_account_input_categ = models.ForeignKey('AccountAccountTemplate', models.DO_NOTHING, blank=True, null=True)
    #property_stock_account_output_categ = models.ForeignKey('AccountAccountTemplate', models.DO_NOTHING, blank=True, null=True)
    #property_stock_valuation_account = models.ForeignKey('AccountAccountTemplate', models.DO_NOTHING, blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'account_chart_template'



#class ResPartnerBank(models.Model):
    #acc_number = models.CharField(max_length=1)
    #sanitized_acc_number = models.CharField(max_length=1, blank=True, null=True)
    #partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    #bank = models.ForeignKey('ResBank', models.DO_NOTHING, blank=True, null=True)
    #sequence = models.IntegerField(blank=True, null=True)
    #currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'res_partner_bank'
        #unique_together = (('sanitized_acc_number', 'company'),)



#class StudentFeesStructure(models.Model):
    #name = models.CharField(max_length=1)
    #code = models.CharField(unique=True, max_length=1)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'student_fees_structure'

#class SchoolSchool(models.Model):
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    #com_name = models.CharField(max_length=1, blank=True, null=True)
    #code = models.CharField(max_length=1)
    #lang = models.CharField(max_length=1, blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'school_school'



#class StandardStandard(models.Model):
    #sequence = models.IntegerField(blank=True, null=True)
    #name = models.CharField(max_length=1)
    #code = models.CharField(max_length=1)
    #description = models.TextField(blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'standard_standard'



#class StandardDivision(models.Model):
    #sequence = models.IntegerField(blank=True, null=True)
    #name = models.CharField(max_length=1)
    #code = models.CharField(max_length=1)
    #description = models.TextField(blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'standard_division'


#class SchoolStandard(models.Model):
    #school = models.ForeignKey('SchoolSchool', models.DO_NOTHING)
    #standard = models.ForeignKey('StandardStandard', models.DO_NOTHING)
    #division = models.ForeignKey('StandardDivision', models.DO_NOTHING)
    #medium = models.ForeignKey('StandardMedium', models.DO_NOTHING)
    #user = models.ForeignKey('SchoolTeacher', models.DO_NOTHING, blank=True, null=True)
    #color = models.IntegerField(blank=True, null=True)
    #cmp = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    #name = models.CharField(max_length=1, blank=True, null=True)
    #capacity = models.IntegerField(blank=True, null=True)
    #total_students = models.IntegerField(blank=True, null=True)
    #remaining_seats = models.IntegerField(blank=True, null=True)
    #class_room = models.ForeignKey('ClassRoom', models.DO_NOTHING, blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'school_standard'

#class StandardMedium(models.Model):
    #sequence = models.IntegerField(blank=True, null=True)
    #name = models.CharField(max_length=1)
    #code = models.CharField(max_length=1)
    #description = models.TextField(blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'standard_medium'




#class ClassRoom(models.Model):
    #name = models.CharField(max_length=1, blank=True, null=True)
    #number = models.CharField(max_length=1, blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'class_room'

#class HrEmployee(models.Model):
    #name = models.CharField(max_length=1, blank=True, null=True)
    #active = models.NullBooleanField()
    #address_home = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    #country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True)
    #gender = models.CharField(max_length=1, blank=True, null=True)
    #marital = models.CharField(max_length=1, blank=True, null=True)
    #birthday = models.DateField(blank=True, null=True)
    #ssnid = models.CharField(max_length=1, blank=True, null=True)
    #sinid = models.CharField(max_length=1, blank=True, null=True)
    #identification_id = models.CharField(max_length=1, blank=True, null=True)
    #passport_id = models.CharField(max_length=1, blank=True, null=True)
    #bank_account = models.ForeignKey('ResPartnerBank', models.DO_NOTHING, blank=True, null=True)
    #permit_no = models.CharField(max_length=1, blank=True, null=True)
    #visa_no = models.CharField(max_length=1, blank=True, null=True)
    #visa_expire = models.DateField(blank=True, null=True)
    #address = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    #work_phone = models.CharField(max_length=1, blank=True, null=True)
    #mobile_phone = models.CharField(max_length=1, blank=True, null=True)
    #work_email = models.CharField(max_length=1, blank=True, null=True)
    #work_location = models.CharField(max_length=1, blank=True, null=True)
    #job = models.ForeignKey('HrJob', models.DO_NOTHING, blank=True, null=True)
    #department = models.ForeignKey('HrDepartment', models.DO_NOTHING, blank=True, null=True)
    #parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    #coach = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    #notes = models.TextField(blank=True, null=True)
    #color = models.IntegerField(blank=True, null=True)
    #resource = models.ForeignKey('ResourceResource', models.DO_NOTHING)
    #message_last_post = models.DateTimeField(blank=True, null=True)
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'hr_employee'


#class ResourceResource(models.Model):
    #name = models.CharField(max_length=1)
    #active = models.NullBooleanField()
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    #resource_type = models.CharField(max_length=1)
    #user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    #time_efficiency = models.FloatField()
    #calendar = models.ForeignKey('ResourceCalendar', models.DO_NOTHING)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'resource_resource'

#class HrJob(models.Model):
    #name = models.CharField(max_length=1)
    #expected_employees = models.IntegerField(blank=True, null=True)
    #no_of_employee = models.IntegerField(blank=True, null=True)
    #no_of_recruitment = models.IntegerField(blank=True, null=True)
    #no_of_hired_employee = models.IntegerField(blank=True, null=True)
    #description = models.TextField(blank=True, null=True)
    #requirements = models.TextField(blank=True, null=True)
    #department = models.ForeignKey('HrDepartment', models.DO_NOTHING, blank=True, null=True)
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    #state = models.CharField(max_length=1)
    #message_last_post = models.DateTimeField(blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)
    #address = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    #manager = models.ForeignKey('HrEmployee', models.DO_NOTHING, blank=True, null=True)
    #user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    #hr_responsible = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    #alias = models.ForeignKey('MailAlias', models.DO_NOTHING)
    #color = models.IntegerField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'hr_job'
        #unique_together = (('name', 'company', 'department'),)


#class HrDepartment(models.Model):
    #name = models.CharField(max_length=1)
    #complete_name = models.CharField(max_length=1, blank=True, null=True)
    #active = models.NullBooleanField()
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    #parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    #manager = models.ForeignKey('HrEmployee', models.DO_NOTHING, blank=True, null=True)
    #note = models.TextField(blank=True, null=True)
    #color = models.IntegerField(blank=True, null=True)
    #message_last_post = models.DateTimeField(blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'hr_department'


#class SchoolTeacher(models.Model):
    #employee = models.ForeignKey('HrEmployee', models.DO_NOTHING)
    #standard = models.ForeignKey('SchoolStandard', models.DO_NOTHING, blank=True, null=True)
    #stand = models.ForeignKey('StandardStandard', models.DO_NOTHING, blank=True, null=True)
    #school = models.ForeignKey('SchoolSchool', models.DO_NOTHING, blank=True, null=True)
    #department = models.ForeignKey('HrDepartment', models.DO_NOTHING, blank=True, null=True)
    #job = models.ForeignKey('HrJob', models.DO_NOTHING, blank=True, null=True)
    #is_parent = models.NullBooleanField()
    #stu_parent = models.ForeignKey('SchoolParent', models.DO_NOTHING, blank=True, null=True)
    #phone_numbers = models.CharField(max_length=1, blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'school_teacher'


#class ParentRelation(models.Model):
    #name = models.CharField(max_length=1)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'parent_relation'


#class SchoolParent(models.Model):
    #partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    #relation = models.ForeignKey('ParentRelation', models.DO_NOTHING, blank=True, null=True)
    #teacher = models.ForeignKey('SchoolTeacher', models.DO_NOTHING, blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'school_parent'


#class StudentPayslip(models.Model):
    #fees_structure = models.ForeignKey('StudentFeesStructure', models.DO_NOTHING, blank=True, null=True)
    #standard = models.ForeignKey('SchoolStandard', models.DO_NOTHING, blank=True, null=True)
    #division = models.ForeignKey('StandardDivision', models.DO_NOTHING, blank=True, null=True)
    #medium = models.ForeignKey('StandardMedium', models.DO_NOTHING, blank=True, null=True)
    #register = models.ForeignKey('StudentFeesRegister', models.DO_NOTHING, blank=True, null=True)
    #name = models.CharField(max_length=1, blank=True, null=True)
    #number = models.CharField(max_length=1, blank=True, null=True)
    #student = models.ForeignKey('StudentStudent', models.DO_NOTHING, blank=True, null=True)
    #date = models.DateField(blank=True, null=True)
    #total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #state = models.CharField(max_length=1, blank=True, null=True)
    #journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True)
    #paid_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #due_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    #move = models.ForeignKey('AccountMove', models.DO_NOTHING, blank=True, null=True)
    #payment_date = models.DateField(blank=True, null=True)
    #type = models.CharField(max_length=1)
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'student_payslip'
        #unique_together = (('student', 'date', 'state'),)


#class StudentFeesRegister(models.Model):
    #name = models.CharField(max_length=1)
    #date = models.DateField()
    #number = models.CharField(max_length=1, blank=True, null=True)
    #state = models.CharField(max_length=1, blank=True, null=True)
    #journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True)
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    #fees_structure = models.ForeignKey('StudentFeesStructure', models.DO_NOTHING, db_column='fees_structure', blank=True, null=True)
    #standard = models.ForeignKey('StandardStandard', models.DO_NOTHING, blank=True, null=True)
    #division = models.ForeignKey('StandardDivision', models.DO_NOTHING, blank=True, null=True)
    #medium = models.ForeignKey('StandardMedium', models.DO_NOTHING, blank=True, null=True)
    #category = models.ForeignKey('StudentCast', models.DO_NOTHING, blank=True, null=True)
    #payment_date = models.DateField(blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)
    #fine_type = models.ForeignKey('LateFeesRule', models.DO_NOTHING, blank=True, null=True)
    #fine_type_0 = models.CharField(db_column='fine_type', max_length=1, blank=True, null=True)  # Field renamed because of name conflict.
    #fine_rate = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'student_fees_register'


#class StudentFeesRegister(models.Model):
    #name = models.CharField(max_length=1)
    #date = models.DateField()
    #number = models.CharField(max_length=1, blank=True, null=True)
    #state = models.CharField(max_length=1, blank=True, null=True)
    #journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True)
    #company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    #fees_structure = models.ForeignKey('StudentFeesStructure', models.DO_NOTHING, db_column='fees_structure', blank=True, null=True)
    #standard = models.ForeignKey('StandardStandard', models.DO_NOTHING, blank=True, null=True)
    #division = models.ForeignKey('StandardDivision', models.DO_NOTHING, blank=True, null=True)
    #medium = models.ForeignKey('StandardMedium', models.DO_NOTHING, blank=True, null=True)
    #category = models.ForeignKey('StudentCast', models.DO_NOTHING, blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)
    #payment_date = models.DateField(blank=True, null=True)
    #fine_type = models.ForeignKey('LateFeesRule', models.DO_NOTHING, blank=True, null=True)
    #fine_type_0 = models.CharField(db_column='fine_type', max_length=1, blank=True, null=True)  # Field renamed because of name conflict.
    #fine_rate = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'student_fees_register'
        

#class StudentCast(models.Model):
    #name = models.CharField(max_length=1)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'student_cast'
        

#class FineTypes(models.Model):
    #name = models.CharField(max_length=1, blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'fine_types'


#class LateFeesRule(models.Model):
    #fine_type = models.ForeignKey('FineTypes', models.DO_NOTHING, blank=True, null=True)
    #name = models.CharField(max_length=1, blank=True, null=True)
    #fine_type_0 = models.CharField(db_column='fine_type', max_length=1, blank=True, null=True)  # Field renamed because of name conflict.
    #fine_rate = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    #frequency = models.IntegerField(blank=True, null=True)
    #create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    #create_date = models.DateTimeField(blank=True, null=True)
    #write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    #write_date = models.DateTimeField(blank=True, null=True)

    #class Meta:
        #managed = False
        #db_table = 'late_fees_rule'
