from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Product
from .serializers import ProductListSerializer, ProductDetailSerializer


class ProductViewSet(viewsets.ViewSet):
    @staticmethod
    def list(request):
        queryset = Product.objects.filter(available=True)
        serializer = ProductListSerializer(queryset, many=True)
        return Response(serializer.data)

    @staticmethod
    def retrieve(self, request, pk=None):
        queryset = Product.objects.filter(available=True)
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)
