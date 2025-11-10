from django.shortcuts import render
from rest_framework import viewsets, permissions, status, filters
from .models import Order
from .serializers import OrderSerializer
from users.permissions import IsAdminRole
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponse
import csv

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id','user__email']

    def get_permissions(self):
        if self.action in ['list','retrieve', 'update', 'partial_update']:
            # list/retrieve allowed to admin only (for admin endpoints)
            return [permissions.IsAuthenticated(), IsAdminRole()]
        if self.action == 'create':
            return [permissions.IsAuthenticated()]  # user checkout
        return [permissions.IsAuthenticated()]

    @action(detail=True, methods=['put'], permission_classes=[permissions.IsAuthenticated, IsAdminRole])
    def status(self, request, pk=None):
        order = self.get_object()
        status_value = request.data.get('status')
        allowed = ['Pending','Processing','Shipped','Delivered','Cancelled']
        if status_value not in allowed:
            return Response({'error':'Invalid status'}, status=status.HTTP_400_BAD_REQUEST)
        order.status = status_value
        order.save()
        return Response({'success': True, 'status': order.status})

    @action(detail=False, methods=['post'], permission_classes=[permissions.IsAuthenticated, IsAdminRole])
    def export(self, request):
        order_ids = request.data.get('order_ids', [])
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="orders.csv"'
        writer = csv.writer(response)
        writer.writerow(['order_id','user_email','total_price','status','created_at'])
        qs = self.get_queryset().filter(id__in=order_ids) if order_ids else self.get_queryset()
        for o in qs:
            writer.writerow([o.id, o.user.email if o.user else '', o.total_price, o.status, o.created_at])
        return response

# Create your views here.
