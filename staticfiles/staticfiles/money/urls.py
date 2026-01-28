from django.urls import path
from . import views

app_name = 'money'

urlpatterns = [
    path('money_home/',views.money_home_view,name="money_home"),
    path('income/',views.income_view,name="income"),
    path('expenditure/',views.expenditure_view,name="expenditure"),
]