from rest_framework import serializers
from rest_framework.reverse import reverse
from .validators import validate_title
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field = 'pk'
    )
    # email = serializers.EmailField(write_only=True)
    title = serializers.CharField(validators=[validate_title])

    class Meta:
        model = Product
        fields = [
            # 'email',
            'url',
            'edit_url',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]

    # custom validation
    # def validate_<fields name> ...
    def validate_title(self, value):
        request = self.context.get('request')
        user = request.user
        qs = Product.objects.filter(user=user, title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f'{value} is already product name')
        return value


    # def create(self, validated_data):
    #     # return Product.objects.create(**validated_data)
    #     email = validated_data.pop('email')
    #     obj = super().create(**validated_data)
    #     print(email, obj)
    #     return obj

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('product-edit', kwargs={'pk': obj.pk}, request=request)

    def get_my_discount(self, obj):
        try:
            return obj.get_discount()
        except:
            return None