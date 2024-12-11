from django.urls import path
from .views import expense_list, add_expense, update_expense, delete_expense

urlpatterns = [
    path('', views.expense_list, name='expense_list'),
]