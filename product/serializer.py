from rest_framework import serializers

from product.models import Product


class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'text', 'price')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        return rep


class CreateProductSerializer (serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

