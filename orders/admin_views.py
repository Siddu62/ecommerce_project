# orders/admin_views.py
from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdminRole
from .models import Order
from .serializers import OrderSerializer
from django.db.models import Q
from django.http import HttpResponse
import csv, io
from datetime import datetime

class AdminOrderViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Admin list + retrieve + extra actions: status update, add note, export
    """
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'user__email']

    def get_permissions(self):
        return [IsAuthenticated(), IsAdminRole()]

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset()
        # filters: status, date_from, date_to, q (email/orderId)
        status_q = request.query_params.get('status')
        date_from = request.query_params.get('date_from')
        date_to = request.query_params.get('date_to')
        q = request.query_params.get('q')
        if status_q:
            qs = qs.filter(status=status_q)
        if date_from:
            try:
                df = datetime.fromisoformat(date_from)
                qs = qs.filter(created_at__gte=df)
            except:
                pass
        if date_to:
            try:
                dt = datetime.fromisoformat(date_to)
                qs = qs.filter(created_at__lte=dt)
            except:
                pass
        if q:
            qs = qs.filter(Q(user__email__icontains=q) | Q(id__icontains=q))
        page = self.paginate_queryset(qs)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['put'])
    def status(self, request, pk=None):
        order = self.get_object()
        status_val = request.data.get('status')
        allowed = ['Pending','Processing','Shipped','Delivered','Cancelled']
        if status_val not in allowed:
            return Response({'error':'Invalid status'}, status=status.HTTP_400_BAD_REQUEST)
        order.status = status_val
        order.save()
        return Response({'success': True, 'status': order.status})

    @action(detail=True, methods=['put'])
    def notes(self, request, pk=None):
        order = self.get_object()
        note = request.data.get('note', '')
        order.admin_notes = (order.admin_notes or '') + f"\n{datetime.now().isoformat()} - {note}"
        order.save()
        return Response({'success': True, 'notes': order.admin_notes})

    @action(detail=False, methods=['post'])
    def export(self, request):
        ids = request.data.get('order_ids', [])
        qs = self.get_queryset().filter(id__in=ids) if ids else self.get_queryset()
        # build csv
        buffer = io.StringIO()
        writer = csv.writer(buffer)
        writer.writerow(['order_id','user_email','total_price','status','created_at'])
        for o in qs:
            writer.writerow([o.id, o.user.email if o.user else '', str(o.total_price), o.status, o.created_at.isoformat()])
        resp = HttpResponse(buffer.getvalue(), content_type='text/csv')
        resp['Content-Disposition'] = 'attachment; filename=orders_export.csv'
        return resp
