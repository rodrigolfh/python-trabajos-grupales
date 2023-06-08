from django.contrib import admin
from account.models import Account #linea agregada manual
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AccountInLine(admin.StackedInline):
    model = Account
    can_delete = False
    #evita borrar cuentas si el usuario no es eliminado. van de la mano.
    verbose_name_plural = 'Accounts'

class CustomizedUserAdmin(UserAdmin):
    inlines = (AccountInLine, )

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)
#admin.site.register(Account)