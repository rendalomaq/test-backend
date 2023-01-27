from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductListSerializer(ProductSerializer):
    price = serializers.IntegerField(read_only=True)
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'stock', 'category']
