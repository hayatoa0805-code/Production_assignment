from django.contrib import admin
from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('events_home/', views.events_home_view, name='events_home'),
    path('add/', views.event_add_view, name='events_add'),
    path('image/<int:event_id>/', views.event_image_view, name='events_image'),
    path('detail<int:event_id>',views.events_detail_view,name='events_detail'),
    path('detail/<int:event_id>/goods', views.goods_detail_view, name='goods_detail'),
    path('<int:event_id>/goods/<int:goods_id>/plus/', views.goods_plus_view, name='goods_plus'),
    path('<int:event_id>/goods/<int:goods_id>/minus/', views.goods_minus_view, name='goods_minus'),
]