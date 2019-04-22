from django.contrib import admin
from modules.expense.models import Expense


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('school','fee','books','uniform','shoes','transport','lunch','total_amount','date_modified')

admin.site.register(Expense, ExpenseAdmin)

