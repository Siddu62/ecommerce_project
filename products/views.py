from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from .models import Product
from .serializers import ProductSerializer
from users.permissions import IsAdminRole

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(is_deleted=False).order_by('-created_at')
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'slug', 'category']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsAdminRole()]
        return [permissions.AllowAny()]

