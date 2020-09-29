from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from API import views
from django.conf.urls import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'employee', views.EmployeeViewSet)
router.register(r'accessory', views.AccessoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('employee.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
