from django.urls import path
from . import views

app_name = 'oshis'

urlpatterns = [
    path('oshis_home/', views.oshi_home_view, name='oshi_home'),
    path('oshi_add/', views.oshi_add_view, name='oshi_add'),
    path('oshi_detail/<int:pk>/',views.oshi_detail_view,name="oshi_detail"),
    path('oshi_edit/<int:pk>/',views.oshi_edit_view,name="oshi_edit"),
    path('oshi_delete/<int:pk>/', views.oshi_delete_view, name="oshi_delete"),
]