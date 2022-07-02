from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CRMUser


class AccountsAdmin(UserAdmin):
    model = CRMUser
    fieldsets = *UserAdmin.fieldsets, ('Role', {'fields': ('is_manager', )})


admin.site.register(CRMUser, AccountsAdmin)

