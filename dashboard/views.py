from django.shortcuts import render, redirect
from .models import Income, Expense
from .forms import IncomeForm, ExpenseForm
from django.db.models import Sum
from decimal import Decimal

# Dashboard View - Summary of Income & Expenses
def dashboard(request):
    total_income = Income.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    total_expenses = Expense.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    estimated_tax = total_income * Decimal ("0.20")  # Assume 20% tax rate
    estimated_ni = total_income *  Decimal ("0.09")  # Assume 9% NI rate

    context = {
        'total_income': total_income,
        'total_expenses': total_expenses,
        'estimated_tax': estimated_tax,
        'estimated_ni': estimated_ni,
        'net_income': total_income - (estimated_tax + estimated_ni + total_expenses)
    }
    return render(request, 'dashboard/index.html', context)

# Add Income View - Handles Income Form Submission
def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = IncomeForm()
    return render(request, 'dashboard/income.html', {'form': form})

# Add Expense View - Handles Expense Form Submission
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ExpenseForm()
    return render(request, 'dashboard/expenses.html', {'form': form})
