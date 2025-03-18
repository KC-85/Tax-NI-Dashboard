from django.urls import path
from . import views
from django.conf.urls import handler400, handler403, handler404, handler500
from dashboard import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Homepage (Main Dashboard)
    path('income/', views.add_income, name='add_income'),  # Income Entry Page
    path('expenses/', views.add_expense, name='add_expense'),  # Expenses Entry Page
   
    handler400 = "dashboard.views.error_400"
    handler403 = "dashboard.views.error_403"
    handler404 = "dashboard.views.error_404"
    handler500 = "dashboard.views.error_500"
]
