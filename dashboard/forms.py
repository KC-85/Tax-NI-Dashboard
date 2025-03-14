from django import forms
from .models import Income, Expense

# Form for Income
class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['date', 'amount']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

# Form for Expenses
class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['description', 'date', 'amount']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
