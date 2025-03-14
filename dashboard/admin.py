from django.contrib import admin
from .models import Income, Expense

# Customizing the admin panel display
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('date', 'amount')  # Show these fields in the admin panel
    search_fields = ('date',)  # Enable search by date
    list_filter = ('date',)  # Add a filter sidebar for date

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('description', 'date', 'amount')
    search_fields = ('description',)
    list_filter = ('date',)

# Registering models with custom admin views
admin.site.register(Income, IncomeAdmin)
admin.site.register(Expense, ExpenseAdmin)
