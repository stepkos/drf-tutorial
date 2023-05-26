from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = title
        serializer.save(content=content)


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'

    # Product.objects.get(pk=1)


class ProductListAPIView(generics.ListAPIView):
    '''
    Not gonna use this method
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'

    # Product.objects.get(pk=1)
