from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, \
    CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product
from product.serializer import ProductsListSerializer, ProductDetailSerializer, CreateProductSerializer


# class ProductsListView(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductsListSerializer
#
#
# class ProductDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductDetailSerializer
#
#
# class ProductDetailView(RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductDetailSerializer
#
#
# class ProductsListCreateView(ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductsListSerializer
#
# @api_view
# def Product_list(request):
#     pubs = Product.objects.all()
#     serializer = ProductsListSerializer(pubs, many=True)
#     return Response(serializer.data)
#
#
# class ProductListView(APIView):
#     def get(self, request):
#         pubs = Product.objects.all()
#         serializer = ProductsListSerializer(pubs, many=True)
#         return Response(serializer.data)


class ProductsListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsListSerializer


class ProductDetailsView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class CreateProductView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer


class UpdateProductView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer


class DeleteProductView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.action == 'List':
            return ProductsListSerializer
        elif self.action == 'retrieve':
            return ProductDetailSerializer
        return CreateProductSerializer
