from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'price': {'label': 'Product Price'},
            'name': {'label': 'Product Name'},
        }