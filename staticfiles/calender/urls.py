from django.urls import path
from . import views

app_name = 'calender'

urlpatterns = [
    path("", views.calendar_view, name="calendar_home"),
    path("<int:year>/<int:month>/", views.calendar_view, name="calendar_home"),
    path("<int:year>/<int:month>/minus/", views.month_minus_view, name="month_minus"),
    path("<int:year>/<int:month>/plus/", views.month_plus_view, name="month_plus"),
]