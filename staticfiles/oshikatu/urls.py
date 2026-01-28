from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), 
    path('home/', views.home_view, name='home'),
    path('accounts/', include('accounts.urls')), 
    path('calender/', include('calender.urls')),
    path('events/', include('events.urls')),
    path('plan/', include('plan.urls')),
    path('oshis/', include('oshis.urls')),
    path('money/',include('money.urls')),
    path('goods/', include('goods.urls')),
    path('settings/', views.settings_view, name='settings'),
    path('test/', views.test_view, name='test'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)