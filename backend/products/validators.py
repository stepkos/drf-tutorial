from rest_framework import serializers
from .models import Product
from rest_framework.validators import UniqueValidator

def validate_title(value):
    qs = Product.objects.filter(title__iexact=value)
    if qs.exists():
        raise serializers.ValidationError(f'{value} is already product name')
    return value


unique_product_title = UniqueValidator(queryset=Product.objects.all())