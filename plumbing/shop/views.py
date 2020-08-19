from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductListSerializer, ProductDetailSerializer


class ProductListView(APIView):
    """Вывод списка товаров"""
    def get(self, request):
        products = Product.objects.filter(available=True)
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetailView(APIView):
    """Вывод карточки товара"""
    def get(self, request, pk):
        product = Product.objects.get(id=pk, available=True)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)
