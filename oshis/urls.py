from django.urls import path
from . import views

app_name = 'oshis'

urlpatterns = [
    path('oshis_home/', views.home_view, name='oshi_home'),
    path('oshi_detail/<int:pk>',views.oshi_detail_view,name="oshi_detail"),
    path('add/', views.add_view, name='oshi_add'),
]