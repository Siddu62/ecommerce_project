from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    # 🏠 Frontend Pages
    path('', TemplateView.as_view(template_name='products_list.html'), name='product_list'),
    path('cart/', TemplateView.as_view(template_name='cart.html'), name='cart'),
    # 🧭 Admin Django Panel
    path('admin-django/', admin.site.urls),

    # 🔐 API Endpoints
    path('api/auth/', include('users.urls')),
    path('api/', include('products.urls')),
    path('api/', include('orders.urls')),

    # 🧰 Simple Admin UI Pages (custom HTML templates)
    path('admin/login/', TemplateView.as_view(template_name='admin_login.html'), name='admin_login'),
    path('admin/dashboard/', TemplateView.as_view(template_name='admin_dashboard.html'), name='admin_dashboard'),
    path('admin/products/', TemplateView.as_view(template_name='admin_products.html'), name='admin_products'),
    path('admin/products/new/', TemplateView.as_view(template_name='admin_product_form.html'), name='admin_product_new'),
    path('admin/orders/', TemplateView.as_view(template_name='admin_orders.html'), name='admin_orders'),
    path('admin/orders/<int:id>/', TemplateView.as_view(template_name='admin_order_detail.html'), name='admin_order_detail'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
