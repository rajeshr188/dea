from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Account)
admin.site.register(models.AccountType)
admin.site.register(models.EntityType)
admin.site.register(models.Ledger)
admin.site.register(models.TransactionType_DE)
admin.site.register(models.TransactionType_Ext)
admin.site.register(models.LedgerTransaction)
admin.site.register(models.LedgerStatement)
admin.site.register(models.AccountType_Ext)
admin.site.register(models.AccountTransaction)
admin.site.register(models.AccountStatement)

