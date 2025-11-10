# products/admin_views.py
from rest_framework import viewsets, filters, status
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdminRole
from .models import Product
from .serializers import ProductSerializer
import csv, io

class AdminProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'slug', 'category']

    def get_permissions(self):
        return [IsAuthenticated(), IsAdminRole()]

    def destroy(self, request, *args, **kwargs):
        # soft-delete implementation — mark is_deleted True
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['post'])
    def import_csv(self, request):
        """
        POST /api/admin/products/import/  (file: csv)
        CSV expected columns: name, category, price, stock, weight, description
        """
        file = request.FILES.get('file')
        if not file:
            return Response({'error': 'CSV file required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            decoded = file.read().decode('utf-8')
            reader = csv.DictReader(io.StringIO(decoded))
            created = 0
            for row in reader:
                Product.objects.update_or_create(
                    name=row.get('name') or row.get('title'),
                    defaults={
                        'category': row.get('category',''),
                        'price': row.get('price') or 0,
                        'stock': row.get('stock') or 0,
                        'weight': row.get('weight') or 0,
                        'description': row.get('description',''),
                        'is_deleted': False
                    }
                )
                created += 1
            return Response({'success': True, 'processed': created})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# Add this at the very bottom of products/admin_views.py

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdminRole
from orders.models import Order
from products.models import Product
from django.db.models import Sum

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminRole])
def dashboard_stats(request):
    total_orders = Order.objects.count()
    pending_orders = Order.objects.filter(status='Pending').count()
    total_revenue = Order.objects.filter(status='Delivered').aggregate(total=Sum('total_price'))['total'] or 0
    total_products = Product.objects.filter(is_deleted=False).count()

    return Response({
        'total_orders': total_orders,
        'pending_orders': pending_orders,
        'total_revenue': total_revenue,
        'total_products': total_products,
    })
