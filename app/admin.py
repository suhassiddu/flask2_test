# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Banks, Branches

class BankAdmin(admin.ModelAdmin):
    pass

class BranchAdmin(admin.ModelAdmin):
    pass

admin.site.register(Bank, BankAdmin)
admin.site.register(Branch, BranchAdmin)
