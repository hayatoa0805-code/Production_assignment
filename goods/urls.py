from django.urls import path
from . import views

app_name = 'goods'

urlpatterns = [
    path("goods_home/",views.goods_home_view,name="goods_home"),
    path("goods_add",views.goods_add_view,name="goods_add"),
    path('goods/<int:event_id>/add/',views.goods_id_add_view,name="goods_id_add"),
    path('events/<int:event_id>/edit/<int:goods_id>/', views.goods_edit_view, name='goods_edit'),
    path('events/<int:event_id>/delete/<int:goods_id>/', views.goods_delete_view, name='goods_delete'),
]