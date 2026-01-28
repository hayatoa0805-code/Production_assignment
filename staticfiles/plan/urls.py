from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("plan_home/",views.plan_home_view,name="plan_home")
]