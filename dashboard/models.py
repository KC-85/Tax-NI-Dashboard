from django.db import models
from django.utils.timezone import now

# Model for Income Tracking
class Income(models.Model):
    date = models.DateField(default=now)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=450.00)

    def __str__(self):
        return f"{self.date} - £{self.amount}"

# Model for Expense Tracking
class Expense(models.Model):
    description = models.CharField(max_length=255)
    date = models.DateField(default=now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.description}: £{self.amount}"
