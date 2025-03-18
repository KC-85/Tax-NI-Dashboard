from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Homepage (Main Dashboard)
    path('income/', views.add_income, name='add_income'),  # Income Entry Page
    path('expenses/', views.add_expense, name='add_expense'),  # Expenses Entry Page
]
