from rest_framework.routers import DefaultRouter
from .views import ProductViewSet
from django.urls import path, include
from .admin_views import dashboard_stats
from .admin_views import dashboard_stats

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += [ path('admin/dashboard-stats/', dashboard_stats) ]
