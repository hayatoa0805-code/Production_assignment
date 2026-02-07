from django.urls import path
from . import views

app_name = 'money'

urlpatterns = [
    path('money_home/',views.money_home_view,name="money_home"),

    path('income/',views.income_view,name="income"),
    path('income/edit/<int:pk>/',views.income_edit_view,name="income_edit"),
    path('income/delete/<int:pk>/',views.income_delete_view,name="income_delete"),

    path('expenditure/',views.expenditure_view,name="expenditure"),
    path('expenditure/edit/<int:pk>/',views.expenditure_edit_view,name="expenditure_edit"),
    path('expenditure/delete/<int:pk>/',views.expenditure_delete_view,name="expenditure_delete"),
]